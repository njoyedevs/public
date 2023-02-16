# Import render_template from flask 
from flask import render_template, request, redirect

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

# Create create_friend route that will allow for input and save to database
@app.route('/create_friend', methods=["POST"])
def create_friend():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Friend.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')