# Import render_template from flask 
from flask import render_template

# import the Friend class from friend.py to generate Friend objects
from flask_app.models.friend import Friend

# Import app variable server.py to generate instance of Flask
from flask_app import app

# Create root route that will get all data from Friend's class and render in template
@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)