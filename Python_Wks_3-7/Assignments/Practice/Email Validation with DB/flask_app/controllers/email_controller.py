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
    
    if User.get_recent() == False:
        return redirect('/')
    else:
        return render_template("success.html", emails=User.get_all(), email=User.get_recent())

@app.route('/delete', methods=["POST"])
def delete():
    
    data = {
        'id': request.form['id']
    }
    
    User.delete(data)
    return redirect("/success")