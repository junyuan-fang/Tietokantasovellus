from operator import truediv
import secrets
from flask.templating import render_template
from db import db
from flask import session,request

def get_forum_id(message_id):
    sql= """SELECT T.forum_id
        FROM messages M, topic T
        WHERE M.topic_id=T.topic_id
        AND M.message_id=:message_id"""
    result=db.session.execute(sql,{"message_id":message_id})
    forum_id=result.fetchone()[0]
    return forum_id
def get_topic_id(message_id):
    sql= """SELECT M.topic_id
        FROM messages M
        WHERE M.message_id=:message_id"""
    result=db.session.execute(sql,{"message_id":message_id})
    topic_id=result.fetchone()[0]
    return topic_id

def remove_message(message_id):
    sql="""
        UPDATE messages
        SET visibility = False
        WHERE message_id=:message_id
    """
    db.session.execute(sql,{"message_id":message_id})
    db.session.commit()

def get_content(message_id):
    sql="""SELECT content
        FROM messages
        WHERE message_id=:message_id"""
    result=db.session.execute(sql, {"message_id":message_id})
    return result.fetchone()[0]

#change content, change user_id if the ower changes it, change time stamp
def edit_message(message_id, content, user_id):
    sql="""
        UPDATE messages
        SET content=:content,
            user_id=:user_id,
            created_at= NOW()
        WHERE message_id=:message_id"""
    db.session.execute(sql, {"content":content,"user_id":user_id, "message_id":message_id})
    db.session.commit()