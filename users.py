import secrets
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

def login(username,password): 
    sql = "SELECT U.user_id, U.password FROM users U WHERE U.account=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if user:
        if check_password_hash(user.password, password):
            session["user_account"]=username
            session["user_id"]=user.user_id
            session["csrf_token"] = secrets.token_hex(16)
            return True
        return False
    return False

def logout():
    del session["user_id"]
    del session["user_account"]
    del session["csrf_token"]

def user_id():
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
    #sql="SELECT F.forum_id, F.theme, F.public, F.visibility FROM user_forum UF INNER JOIN users U on U.user_id=UF.user_id INNER JOIN forums F on F.forum_id=UF.forum_id WHERE U.user_id=(:user_id) OR F.public=True"
    sql = """SELECT  FT.public public, FT.theme theme, FT.topic_num topic_num, FT.message_num message_num, FT.time_stamp time_stamp, FT.forum_id forum_id
    FROM user_forum UF
    INNER JOIN users U ON U.user_id=UF.user_id
    INNER JOIN 

    (SELECT F.visibility AS visibility, F.forum_id AS forum_id, F.theme AS theme, F.public, COUNT( TT.topic_id) AS topic_num, SUM(TT.message_num) AS message_num, MAX(TT.time_stamp) AS time_stamp
    FROM forums F
    LEFT JOIN

    (SELECT  T.topic_id AS topic_id, T.title, T.forum_id AS forum_id, COUNT(M.topic_id) AS message_num, MAX(M.created_at) AS time_stamp
    FROM topic T 
    LEFT JOIN messages M ON M.topic_id=T.topic_id 
    WHERE T.visibility=True AND M.visibility=True GROUP BY T.topic_id) AS TT
     
     ON F.forum_id=TT.forum_id AND F.visibility=True
     GROUP BY F.forum_id) AS FT

     on FT.forum_id=UF.forum_id AND FT.visibility=True
     WHERE U.user_id=:user_id or FT.public=True
     ORDER BY FT.time_stamp DESC"""
    result = db.session.execute(sql, {"user_id": user_id})
    return result.fetchall()

def get_message_query(user_id,keyword):
    sql = """
        SELECT FT.account,  FT.content, FT.created_at, FT.title, FT.public, FT.theme
        FROM user_forum UF
        INNER JOIN
        (SELECT U.account, F.forum_id, F.theme, F.public, T.title, M.content, M.created_at
        FROM messages M, topic T, users U, forums F
        WHERE M.topic_id=T.topic_id AND U.user_id=M.user_id AND F.forum_id=T.forum_id
                AND T.visibility=True AND M.visibility=True AND F.visibility=True AND
                LOWER(M.content) LIKE LOWER(:keyword)) AS FT
        
        ON UF.forum_id=FT.forum_id
        WHERE UF.user_id=:user_id OR FT.public=True
        """
    result = db.session.execute(sql,{"user_id":user_id, "keyword": f"%{keyword}%"})
    return  result.fetchall()

def user_in_forum(user_id, forum_id):
    sql = """SELECT UF.isOwner
            FROM user_forum UF
            WHERE UF.forum_id=:forum_id AND UF.user_id=:user_id
        """
    result = db.session.execute(sql,{"user_id":user_id, "forum_id":forum_id})
    value = result.fetchone()
    if value:
        return True
    return False

def is_owner(user_id, forum_id):
    sql = """SELECT UF.isOwner
            FROM user_forum UF
            WHERE UF.forum_id=:forum_id AND UF.user_id=:user_id
        """
    result = db.session.execute(sql,{"user_id":user_id, "forum_id":forum_id})
    value = result.fetchone()
    if value:
        return value[0]
    return False

def is_topic_owner(user_id, topic_id):
    sql = """SELECT T.user_id
            FROM topic T
            WHERE T.topic_id=:topic_id AND T.user_id=:user_id
        """
    result = db.session.execute(sql,{"user_id":user_id, "topic_id":topic_id})
    value = result.fetchone()
    if value:
        return True
    return False

def is_message_owner(user_id, message_id):
    sql= """SELECT M.user_id
            FROM messages M
            WHERE M.message_id=:message_id AND M.user_id=:user_id
        """
    result = db.session.execute(sql,{"user_id":user_id, "message_id":message_id})
    value = result.fetchone()
    if value:
        return True
    return False

#incude the situation that user is not found
def get_user_id(user_account):
    sql="""
        SELECT U.user_id
        FROM users U
        WHERE U.account=:user_account
        """
    result = db.session.execute(sql,{"user_account":user_account})
    value = result.fetchone()
    return value

def get_user_account(user_id):
    sql="""
        SELECT U.account
        FROM users U
        WHERE U.user_id=:user_id
        """
    result = db.session.execute(sql,{"user_id":user_id})
    value = result.fetchone()[0]
    return value

