from operator import truediv
import secrets
from flask.templating import render_template
from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password): 
    sql="SELECT U.user_id, U.password FROM users U WHERE U.account=:username"
    result=db.session.execute(sql, {"username": username})
    user=result.fetchone()
    if user:
        if check_password_hash(user.password, password):
            session["user_account"]=username
            session["user_id"]=user.user_id
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False
    else:
        return False

def logout():
    del session["user_id"]
    del session["user_account"]
    del session["csrf_token"]

def user_id():
    #print("user_id: ", session.get("user_id", 0))
    return session.get("user_id", 0)

#return the empty string, if user_account not found
def user_account():
    return session.get("user_account", "")

def register(username, password):
    hash_value=generate_password_hash(password)
    try:
        sql = "INSERT INTO users (account, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
    except:
        return False
    return login(username,password)

def get_forums(user_id):
    #SELECT-line need to be changed later, because time stamp is not included
    # sql = "SELECT F.theme, F.public"\
    #       "FROM user_forum UF"\
    #       "INNER JOIN users U on U.user_id=UF.user_id"\
    #       "INNER JOIN forums F on F.forum_id=UF.forum_id"\
    #       "WHERE U.user_id=: user_id"
    sql = "SELECT F.forum_id, F.theme, F.public, F.visibility FROM user_forum UF INNER JOIN users U on U.user_id=UF.user_id INNER JOIN forums F on F.forum_id=UF.forum_id WHERE U.user_id=(:user_id)"
    result = db.session.execute(sql, {"user_id": user_id})
    return result.fetchall()
        