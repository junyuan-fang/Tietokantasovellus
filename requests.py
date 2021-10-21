from operator import truediv
import secrets
from flask.templating import render_template
from db import db
from flask import session,request

from users import user_in_forum


def add_request(user_id1,user_id2,forum_id, owner_id):
    if user_in_forum(user_id2,forum_id):
        return False
    
    try:
        sql="""INSERT INTO request (user_id1, user_id2, forum_id, owner_id, visibility)
                            VALUES ( :user_id1, :user_id2, :forum_id, :owner_id, True)"""
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
        WHERE R.visibility=True AND R.user_id1 = U1.user_id AND R.user_id2 = U2.user_id AND F.forum_id=R.forum_id
            AND R.owner_id=:owner_id
    """
    result=db.session.execute(sql,{"owner_id":owner_id})
    return result.fetchall()

def remove_request(request_id):
    sql= """
        UPDATE request
        SET visibility=False
        WHERE request_id=:request_id
    """
    db.session.execute(sql, {"request_id":request_id})
    db.session.commit()
    return True
    