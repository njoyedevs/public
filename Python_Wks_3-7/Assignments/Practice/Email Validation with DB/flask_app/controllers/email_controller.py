from flask import render_template, redirect, request

from flask_app.models.emails import User

from flask_app import app

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/process', methods=["POST"])
def process():
    print(request.form)
    if not User.validate_user(request.form):

        return redirect('/')

    User.save(request.form)
    
    return redirect("/success")

@app.route('/success')
def results():
    return render_template("success.html", emails=User.get_all(), email=User.get_recent())