from operator import truediv
import secrets
from flask.templating import render_template
from db import db
from flask import session,request


def add_request(user_id1,user_id2,forum_id, owner_id):
    try:
        sql="""INSERT INTO request (user_id1, user_id2, forum_id, owner_id, visibility)
                            VALUES ( :user_id1, :user_id2, :forum_id, :owner_id, True)"""
        db.session.execute(sql,{"user_id1": user_id1, "user_id2":user_id2, "forum_id":forum_id, "owner_id":owner_id})
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False
    