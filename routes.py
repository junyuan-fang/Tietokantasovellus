from app import app
import users
from flask import request, render_template, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        username= request.form["username"]
        passward= request.form["passward"]
        if (users.login(username,passward)):
            return redirect("/")
        else:
            return render_template("error.html",message="Wrong username or passward")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        username = request.form["username"]
        passward1 = request.form["passward1"]
        passward2 = request.form["passward2"]
        if (passward1 != passward2 ):
            return render_template("error.html", message = "Passwords are different")
        if(users.register(username, passward1)):
            return redirect("/")
        else:
            return render_template("error.html", message = "Registration filed")
    






@app.route("/forum") #/forum/<int:id>
def forum():
    return "Working!"
@app.route("/topic") #/topic/<int:id>
def topic():
    return "Working!"