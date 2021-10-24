from operator import truediv
import secrets
from flask.templating import render_template
from db import db
from flask import session,request

#return str
def get_title(topic_id):
    sql = "SELECT T.title FROM topic T WHERE T.topic_id=:topic_id"
    result= db.session.execute(sql, {"topic_id":topic_id})
    title=result.fetchone()[0]
    return title

#return the forum_id where topic belongs to
def get_forum_id(topic_id):
    sql = """SELECT T.forum_id 
        FROM topic T  
        WHERE T.topic_id=:topic_id"""
    result= db.session.execute(sql, {"topic_id":topic_id})
    forum_id=result.fetchone()[0]
    return forum_id

def get_messages(topic_id):
    sql = """SELECT M.message_id, M.topic_id, U.account, M.content, M.created_at, M.visibility 
            FROM messages M
            INNER JOIN users U
            ON U.user_id=M.user_id
            WHERE M.topic_id=:topic_id 
            ORDER BY M.created_at"""
    result = db.session.execute(sql, {"topic_id": topic_id})
    return result.fetchall()

def create_message(topic_id, message):
    try:
        # insert to message
        sql = "INSERT INTO messages ( topic_id, user_id, content, created_at, visibility) VALUES (:topic_id, :user_id, :content, NOW(), :visibility)"
        db.session.execute(sql, {"topic_id":topic_id, "user_id":session["user_id"], "content": message, "visibility": True})
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False

#remove topic, remove message
def remove_topic(topic_id):
    sql = "UPDATE topic SET visibility=FALSE WHERE topic_id=:id"
    db.session.execute(sql, { "id":topic_id })
    sql = "UPDATE messages SET visibility=FALSE WHERE topic_id=:id"
    db.session.execute(sql, { "id":topic_id })
    db.session.commit()

def count_messages(topic_id):
    sql="SELECT COUNT(*) FROM topic T INNER JOIN message M ON M.topic_id= T.topic_id WHERE T.topic_id= :topic_id"
    result=db.session.execute(sql, {"topic_id":topic_id})
    num=result.fetchone()[0]
    return num

def edit_title(topic_id,title):
    sql = "UPDATE topic SET title=:title WHERE topic_id=:topic_id"
    db.session.execute(sql, { "title":title, "topic_id":topic_id })
    db.session.commit()

    