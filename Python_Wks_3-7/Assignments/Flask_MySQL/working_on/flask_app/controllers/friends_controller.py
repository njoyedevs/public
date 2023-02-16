from flask import render_template

# import the class from friend.py
from flask_app.models.friend import Friend

# Import app variable server.py
from flask_app import app

# @app.route("/")
# def index():
#     # call the get all classmethod to get all friends
#     friends = Friend.get_all()
#     print(friends)
#     return render_template("index.html")

@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)