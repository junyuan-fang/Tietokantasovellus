from app import app
#import
from flask import render_template

@app.route("/")
def index():
    return "Working!"
@app.route("/forum") #/forum/<int:id>
def forum():
    return "Working!"
@app.route("/topic") #/topic/<int:id>
def topic():
    return "Working!"