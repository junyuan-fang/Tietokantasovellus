from app import app
import users, forums
from flask import request, render_template, redirect, session, abort

@app.route("/")
def index():
    if users.user_id()==0 :
        return redirect("welcome")
    else:    
        forums_list=users.get_forums(users.user_id())
        return render_template("index.html",forums=forums_list)#, forums=forums_list

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    if request.method == "POST":
        username= request.form["username"]
        passward= request.form["password"]
        if (users.login(username,passward)):
            return redirect("/")
        else:
            return render_template("error.html",message="Wrong username or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    if request.method == "POST":
        
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if username=="":#username can not be empty
            return render_template("error.html", message = "Username can not be empty")
        if (password1 != password2 ):
            return render_template("error.html", message = "Passwords are different")
        if(users.register(username, password1)):
            return redirect("/")
        else:#username exists
            return render_template("error.html", message = "Registration failed")

@app.route("/create_forum", methods = ["GET", "POST"])
def create_forum():
    # if session["csrf_token"] != request.form["csrf_token"]:
    #     abort(403)
    if request.method=="GET":   
        return render_template("create_forum.html")
    if request.method=="POST":
        theme = request.form["theme"]
        public_value = request.form["public"]
        if theme=="":
            return render_template("error.html", message= "Theme can not be empty")
        if(forums.create_forum(theme,public_value)):
            return redirect("/")
        else:
            return render_template("error.html", message = "Registration failed")
        
@app.route("/forum/<int:forum_id>", methods = ["GET", "POST"])
def forum(forum_id):
    #get toppics
    #html can add topics and can delete recent forum
    pass
    return render_template("forum.html")



