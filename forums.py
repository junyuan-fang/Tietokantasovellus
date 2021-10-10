from operator import truediv
import secrets
from flask.templating import render_template
from db import db
from flask import session,request
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
        print(e)
        return False

def remove_forum(forum_id):
    print(forum_id)
    sql = "UPDATE forums SET visibility=FALSE WHERE forum_id=:id"
    db.session.execute(sql, { "id":forum_id })
    db.session.commit()

#return str
def get_theme(forum_id):
    sql = "SELECT F.theme FROM forums F WHERE F.forum_id=:forum_id"
    result = db.session.execute(sql, { "forum_id":forum_id })
    print("THE TYPE OF RESULT IS ",result)
    theme= result.fetchone()[0]
    return theme

def get_topics(forum_id):

    sql = "SELECT T.topic_id, T.title, T.visibility, T.user_id FROM topic T WHERE T.forum_id=:forum_id"
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
        print(e)
        return False

