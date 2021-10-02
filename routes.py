from app import app
import users
from flask import request, render_template, redirect, sessions

@app.route("/")
def index():
    print ("Here",users.user_id())
    if users.user_id()=="":
        return redirect("welcome")
    else:    
        return render_template("index.html")

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
        if (password1 != password2 ):
            return render_template("error.html", message = "Passwords are different")
        if(users.register(username, password1)):
            return redirect("/")
        else:
            return render_template("error.html", message = "Registration filed")
    






@app.route("/forum") #/forum/<int:id>
def forum():
    return "Working!"
@app.route("/topic") #/topic/<int:id>
def topic():
    return "Working!"