from app import app
import users, forums, topics, requests
from flask import request, render_template, redirect, session, abort

@app.route("/")
def index():
    if users.user_id()==0 :
        return redirect("welcome")
    else:
        user_id= users.user_id()   
        forums_list=users.get_forums(users.user_id())
        return render_template("index.html",forums=forums_list, user_id=user_id)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/login",methods=["GET","POST"])
def login():    
    if request.method == "POST":
        username= request.form["username"]
        passward= request.form["password"]
        if (users.login(username,passward)):
            return redirect("/")
        else:
            return render_template("error.html",message="Wrong username or password")
    return render_template("login.html")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods = ["GET", "POST"])
def register():
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
    return render_template("register.html")
    
 
#create forum
@app.route("/create_forum", methods = ["GET", "POST"])
def create_forum():
    if request.method=="POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        theme = request.form["theme"]
        public_value = request.form["public"]
        if theme=="":
            return render_template("error.html", message= "Theme can not be empty")
        if(forums.create_forum(theme,public_value)):
            return redirect("/")
        else:
            return render_template("error.html", message = "Registration failed")  
    return render_template("create_forum.html")

@app.route("/search_messages")
def search_messages():
    return render_template("search_messages.html")

@app.route("/searched_messages")
def searched_messages():
    user_id=users.user_id()
    keyword=request.args["keyword"]
    querys= users.get_message_query(user_id,keyword)
    return render_template("searched_messages.html", querys=querys)

@app.route("/request_show/<int:user_id>")
def show_requests(user_id):
    if  users.user_id()==user_id:#and is owner
        request_list=requests.get_requests(user_id)
        return render_template("request_show.html", requests=request_list)
    else:
        return render_template("error.html",message="No right to see the page")

@app.route("/request/confirm/<int:owner_id>/<int:user_id2>/<int:forum_id>/<int:request_id>")
def request_confirm(owner_id,user_id2,forum_id,request_id):
    if requests.confirm_request(user_id2,forum_id):
        requests.remove_request(request_id)
        return redirect(f"/request_show/{owner_id}")
    else:
        requests.remove_request(request_id)
        return render_template("error.html",message="Confirmation failed")

@app.route("/request/delete/<int:request_id>/<int:owner_id>")
def request_delete(request_id,owner_id):
    requests.remove_request(request_id)
    return redirect(f"/request_show/{owner_id}")

#-----------------------------------------------------------------------------------------
#on the forum page:

#Forum shows topics
@app.route("/forum/<int:forum_id>", methods = ["GET", "POST"])##
def forum(forum_id):
    #get toppics
    #html can add topics and can delete recent forum
    #get forum's topics
    theme=forums.get_theme(forum_id)
    is_public=forums.is_public(forum_id)
    topics_list=forums.get_topics(forum_id)####
    is_owner=users.is_owner(users.user_id(),forum_id)
    return render_template("forum.html", forum_id=forum_id ,theme=theme, topics=topics_list,is_public=is_public,is_owner=is_owner)

#for deleting forums
@app.route("/remove/forum/<int:forum_id>")
def remove_forum(forum_id):
    if users.is_owner(users.user_id(), forum_id):
        forums.remove_forum(forum_id)#recursively
        return redirect("/")
    return render_template("error.html",message=f"You do not have permission to remove '{forums.get_theme(forum_id)}' ")

#create topics
@app.route("/create/topic/<int:forum_id>", methods = ["GET", "POST"])
def create_topic(forum_id):
    if request.method=="POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        topic = request.form["topic"]
        initial_message = request.form["message"]
        
        if initial_message=="":
            return render_template("error.html", message= "Message can not be empty")
        if topic=="":
            return render_template("error.html", message= "Topic can not be empty")
        if(forums.create_topic(topic, initial_message, forum_id)):
            return redirect(f"/forum/{forum_id}")
        #unknow problem
        return render_template("error.html", message = "Failed to create topic")
    return render_template("create_topic.html", forum_id=forum_id)

#edit theme
@app.route("/edit/theme/<int:forum_id>", methods=["GET","POST"])
def edit_theme(forum_id):
    if users.is_owner(users.user_id(), forum_id):
        theme=forums.get_theme(forum_id)
        if request.method=="POST":
            new_theme=request.form["theme"]
            forums.edit_theme(forum_id,new_theme)
            return redirect(f"/forum/{forum_id}")
        return render_template("edit_theme.html", forum_id=forum_id, theme=theme)
        # return render_template()
    return render_template("error.html", message="Permission denied" )


#show users in this forum
@app.route("/forum_users/<int:forum_id>")
def forum_users(forum_id):
    user_id=users.user_id()
    is_owner=users.is_owner(user_id,forum_id)  
    users_list=forums.get_users(forum_id)
    theme=forums.get_theme(forum_id)
    return render_template("forum_users.html",users=users_list, theme=theme,forum_id=forum_id,is_owner=is_owner,user_id=user_id)

#incude making a request
@app.route("/forum_add_users/<int:forum_id>", methods=["GET", "POST"])
def forum_add_user(forum_id):
    theme=forums.get_theme(forum_id)
    if request.method=="POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        user_account2=request.form["user_account"]
        if users.get_user_id(user_account2):
            #if current user is the onwer, user will be added to forum.
            #else if not user, the request will be added
            user_id2=users.get_user_id(user_account2)[0]
            user_id1=users.user_id()
            if users.is_owner(user_id1,forum_id):
                if requests.confirm_request(user_id2,forum_id):
                    return redirect(f"/forum/{forum_id}")
                #else
                return render_template("error.html", message = f"Add {user_account2} to {forums.get_theme(forum_id)} failed")
            #request will be added, because not owner
            owner_id=forums.get_owner_id(forum_id)
            if users.user_in_forum(user_id2,forum_id):
                return render_template("error.html", message = f"User {user_account2} is already in the {theme}")
            if requests.add_request(user_id1,user_id2,forum_id, owner_id):
                return redirect(f"/forum/{forum_id}")
            #for example, same request found
            return render_template("error.html", message = "Create request failed")
        #user2 not found
        return render_template("error.html", message = f"User id {user_account2} not found")
    return render_template("forum_add_users.html",forum_id=forum_id, theme=theme)

@app.route("/remove/forum_user/<int:user_id>/<int:forum_id>")
def remove_forum_user(user_id,forum_id):
    if user_id==forums.get_owner_id(forum_id):
        return render_template("error.html", message="Owner can not be deleted")
    if users.is_owner(users.user_id(), forum_id):
        forums.remove_user_from_forum(user_id,forum_id)
        return redirect(f"/forum_users/{forum_id}")
    return render_template("error.html", message="Permission denied" )

#-----------------------------------------------------------------------------------------
#on the topic page:

#Topic shows messages
@app.route("/topic/<int:topic_id>")
def topic(topic_id):
    title= topics.get_title(topic_id)
    forum_id= topics.get_forum_id(topic_id)
    theme=forums.get_theme(forum_id)
    messages_list=topics.get_messages(topic_id)
    user_id=users.user_id()
    is_owner=users.is_owner(user_id, forum_id)
    is_topic_owner=users.is_topic_owner(user_id,topic_id)
    return render_template("topic.html",title=title, topic_id=topic_id, messages=messages_list,\
                             forum_id=forum_id, theme=theme, is_owner=is_owner, is_topic_owner=is_topic_owner )

#edit title
@app.route("/edit/title/<int:topic_id>", methods=["GET","POST"])
def edit_title(topic_id):
    forum_id= topics.get_forum_id(topic_id)
    user_id=users.user_id()
    is_owner=users.is_owner(user_id, forum_id)
    is_topic_owner=users.is_topic_owner(user_id,topic_id)
    if is_owner or is_topic_owner:
        title= topics.get_title(topic_id)
        if request.method=="POST":
            new_title=request.form["title"]
            topics.edit_title(topic_id,new_title)
            return redirect(f"/topic/{topic_id}")
        return render_template("edit_title.html", topic_id=topic_id, title=title)
    return render_template("error.html", message="Permission denied" )

#for deleting topics
@app.route("/remove/topic/<int:topic_id>")
def remove_topic(topic_id):
    topics.remove_topic(topic_id)
    forum_id= topics.get_forum_id(topic_id)
    return redirect(f"/forum/{forum_id}")

#create message in topic    
@app.route("/create/message/<int:topic_id>", methods = ["GET", "POST"])
def create_message(topic_id):
    if request.method=="GET":
        return render_template("create_message.html", topic_id=topic_id)
    if request.method=="POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        message = request.form["message"]
        if message=="":
            return render_template("error.html", message= "Message can not be empty")
        if(topics.create_message(topic_id, message)):
            return redirect(f"/topic/{topic_id}")
        #unknow problem
        return render_template("error.html", message = "Failed to create topic")
        
#-----------------------------------------------------------------------------------------
#  delete message

