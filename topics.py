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