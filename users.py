from operator import truediv

from flask.templating import render_template
from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password): 
    sql="SELECT U.account, U.password FROM users U WHERE U.account=:username"
    result=db.session.execute(sql, {"username": username})
    user=result.fetchone()
    if user:
        if check_password_hash(user.password, password):
            session["user_id"]=user.account
            return True
        else:
            return False
    else:
        return False

def logout():
    del session["user_id"]

def user_id():
    return session.get("user_id", 0)

def register(username, password):
    hash_value=generate_password_hash(password)
    try:
        sql = "INSERT INTO users (account, password) VALUES (:username, :password)"
        print("ok")
        db.session.execute(sql, {"username": username, "password": hash_value})
        print("here")
        db.session.commit()
        print("true")
    except:
        return False
    return login(username,password)

def user_id():
    return session.get("user_id",0)
        
        