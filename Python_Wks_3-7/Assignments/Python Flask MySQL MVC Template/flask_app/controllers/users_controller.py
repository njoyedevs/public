from flask import render_template

from flask_app.models.users import User

from flask_app import app

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_friends = users)

