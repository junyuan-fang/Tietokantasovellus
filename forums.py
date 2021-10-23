from flask import session
from db import db
#hadle two tables, which are "Forum" and "user_forum" 
def create_forum(theme, public_value):
    try:
        #1.insert to forums
        sql = "INSERT INTO forums (theme, public, visibility) VALUES (:theme, :public, :visibility) RETURNING forum_id" 
        result=db.session.execute(sql,{"theme": theme, "public": public_value, "visibility": True})
        #2. insert to user_forum
        forum_id=result.fetchone()[0]
        sql = "INSERT INTO user_forum (forum_id, user_id, isOwner) VALUES (:forum_id, :user_id, :isOwner)"#user_forum starts
        db.session.execute(sql,{"forum_id":forum_id, "user_id": session["user_id"], "isOwner": True})
        db.session.commit()
        return True
    except Exception as e:
        return False

def remove_forum(forum_id):
    #remove forum
    sql = "UPDATE forums SET visibility=False WHERE forum_id=:id"
    db.session.execute(sql, { "id":forum_id })
    #remove user list
    sql = "DELETE FROM user_forum WHERE forum_id=:forum_id"
    db.session.execute(sql, { "forum_id":forum_id })
    #remove topics
    sql = """
            UPDATE topic T 
            SET visibility=False
            FROM forums F
            WHERE T.forum_id=:forum_id
        """
    db.session.execute(sql, { "forum_id":forum_id })
    #remove messages
    sql ="""
            UPDATE messages M 
            SET visibility=False
            FROM topic T, forums F
            WHERE M.topic_id=T.topic_id AND T.forum_id=:forum_id
        """
    db.session.execute(sql, { "forum_id":forum_id })

    db.session.commit()

#return str
def get_theme(forum_id):
    sql = "SELECT F.theme FROM forums F WHERE F.forum_id=:forum_id"
    result = db.session.execute(sql, { "forum_id":forum_id })
    print("THE TYPE OF RESULT IS ",result)
    theme= result.fetchone()[0]
    return theme

#used inner form
def get_topics(forum_id):
    #SELECT T.topic_id, T.title, T.visibility, T.user_id, counter.num FROM topic T,(SELECT T.topic_id AS topic_id, COUNT(*) AS num FROM topic T INNER JOIN messages M ON M.topic_id=T.topic_id WHERE T.visibility=True AND M.visibility=True GROUP BY T.topic_id ) AS counter WHERE counter.topic_id=T.topic_id;
    inner_form=",(SELECT T.topic_id AS topic_id, COUNT(*) AS num FROM topic T INNER JOIN messages M ON M.topic_id=T.topic_id WHERE T.visibility=True AND M.visibility=True GROUP BY T.topic_id ) AS counter " 
    inner_select=", counter.num"
    inner_where= "AND counter.topic_id=T.topic_id"
    sql = "SELECT T.topic_id, T.title, T.visibility, T.user_id"+inner_select+" FROM topic T"+inner_form+" WHERE T.forum_id=:forum_id "+inner_where
    result = db.session.execute(sql, {"forum_id": forum_id})
    return result.fetchall()
 
#create topic, where include on initial messages
def create_topic(topic, initial_message, forum_id):
    
    try:
        #1. insert to topic
        sql = "INSERT INTO topic (user_id, forum_id, title, visibility) VALUES (:user_id, :forum_id, :topic,:visibility) RETURNING topic_id"
        result=db.session.execute(sql,{"user_id": session["user_id"], "forum_id": forum_id, "topic":topic, "visibility": True})
        #2. insert to message
        topic_id= result.fetchone()[0]
        sql = "INSERT INTO messages ( topic_id, user_id, content, created_at, visibility) VALUES (:topic_id, :user_id, :content, NOW(), :visibility)"
        db.session.execute(sql, {"topic_id":topic_id, "user_id":session["user_id"], "content": initial_message, "visibility": True})
        db.session.commit()
        return True

    except Exception as e:
        return False

def is_public(forum_id):
    sql="""
        SELECT public
        FROM forums F
        WHERE F.forum_id=:forum_id
    """
    result=db.session.execute(sql,{"forum_id":forum_id})
    is_public_=result.fetchone()[0]
    return is_public_

def get_users(forum_id):
    sql="""
        SELECT U.user_id, U.account
        FROM forums F, user_forum UF, users U
        WHERE F.forum_id=UF.forum_id AND UF.user_id=U.user_id
            AND F.forum_id=:forum_id
    """
    result=db.session.execute(sql,{"forum_id":forum_id})
    return result.fetchall()

def get_owner_id(forum_id):
    sql="""
        SELECT UF.user_id
        FROM user_forum UF
        WHERE UF.forum_id=:forum_id AND UF.isOwner=True
        """
    result=db.session.execute(sql,{"forum_id":forum_id})
    return result.fetchone()[0]

def remove_user_from_forum(user_id, forum_id):
    sql = "DELETE FROM user_forum WHERE user_id=:user_id AND forum_id=:forum_id"
    db.session.execute(sql, { "user_id":user_id,"forum_id":forum_id })
    db.session.commit()

def edit_theme(forum_id,theme):
    sql = "UPDATE forums SET theme=:theme WHERE forum_id=:forum_id"
    db.session.execute(sql, { "theme":theme, "forum_id":forum_id })
    db.session.commit()