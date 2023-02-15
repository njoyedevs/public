# Imports the models (backend functinoality)
from flask_app.models.modelName import User

# Import app via __init__.py in flask_app folder
from flask_app import app

# Import necessary class from Flask module
from flask import Flask, render_template, request, redirect

# Set root route that will get all user data in list of dictionaries via User import
@app.route('/')
def index():
    
    # Create variable to house the list of dictionaries sent from User class via database call
    users = User.get_all()
    
    # Render the index.html template with users variable for jinja insertion
    return render_template("index.html", users=users)

# Create new_user route for input of data when adding new user
@app.route('/new_user')
def new_user():
    
    # Render the new_user.html template where users can input data
    return render_template('new_user.html')

# Create create_user route that will call the create function via User class 
# with request.form as argument.  This will XXXXXXXX
@app.route('/create_user', methods=['POST'])
def create_user():
    
    User.create(request.form)
    
    return redirect('/')



