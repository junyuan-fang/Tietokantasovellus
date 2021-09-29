from operator import truediv

from flask.templating import render_template
from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,passward): 
    sql="SELECT U.account, U.passward FROM user U WHERE U.account=:username"
    result=db.session.execute(sql, {"username": username})
    user=result.fetchone()
    if user:
        if check_password_hash(user.password, passward):
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

def register(username, passward):
    hash_value=generate_password_hash(passward)
    try:
        sql = "INSERT INTO users (account, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
    except:
        return False
    return login(username,passward)

def user_id():
    return session.get("user_id",0)
        
        