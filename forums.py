from operator import truediv
import secrets
from flask.templating import render_template
from db import db
from flask import session,request
#hadle two tables, which are "Forum" and "user_forum" 
def create_forum(theme, public_value):
    try:
        sql = "INSERT INTO forums (theme, public, visibility) VALUES (:theme, :public, :visibility) RETURNING forum_id" 
        result=db.session.execute(sql,{"theme": theme, "public": public_value, "visibility": True})
        # db.session.commit()
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

#create topic, where include on initial messages
def create_topic(topic, message):
    pass 
    return True

