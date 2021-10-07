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



