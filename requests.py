from operator import truediv
import secrets
from flask.templating import render_template
from db import db
from flask import session,request

from users import user_in_forum

def add_request(user_id1,user_id2,forum_id, owner_id):
    try:
        sql="""INSERT INTO request (user_id1, user_id2, forum_id, owner_id)
                            VALUES ( :user_id1, :user_id2, :forum_id, :owner_id)"""
        db.session.execute(sql,{"user_id1": user_id1, "user_id2":user_id2, "forum_id":forum_id, "owner_id":owner_id})
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False

#include request_id, user1 account, user2 account, forum theme
def get_requests(owner_id):
    sql="""
        SELECT R.request_id, U1.account AS u1account, U2.account AS u2account, F.theme, R.user_id2, F.forum_id, R.owner_id
        FROM request R, users U1, users U2, forums F
        WHERE R.user_id1 = U1.user_id AND R.user_id2 = U2.user_id AND F.forum_id=R.forum_id
            AND R.owner_id=:owner_id
    """
    result=db.session.execute(sql,{"owner_id":owner_id})
    return result.fetchall()

def remove_request(request_id):
    sql= """
        DELETE FROM request
        WHERE request_id=:request_id
    """
    db.session.execute(sql, {"request_id":request_id})
    db.session.commit()
    return True



def confirm_request(user_id,forum_id):
    # if error, then user might already in the forum
    try:
        if user_in_forum(user_id,forum_id):
            raise Exception
        sql="""INSERT INTO user_forum (user_id, forum_id, isOwner) VALUES (:user_id, :forum_id, False)"""
        db.session.execute(sql,{"user_id":user_id, "forum_id":forum_id})
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False
    