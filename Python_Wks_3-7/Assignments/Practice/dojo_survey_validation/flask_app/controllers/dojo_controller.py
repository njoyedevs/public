from flask import render_template, redirect, request

from flask_app.models.dojos import User

from flask_app import app

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/process', methods=["POST"])
def process():
    print(request.form)
    if not User.validate_ninja(request.form):

        return redirect('/')

    User.save(request.form)
    
    return redirect("/results")

@app.route('/results')
def ninjaShow():
    return render_template("result.html", data=User.get_recent())
