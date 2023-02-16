from flask import render_template, request, redirect

from flask_app.models.users import User

from flask_app import app

# @app.route('/')
# def index():
#     users = User.get_all()
#     print(users)
#     return render_template("index.html", all_friends = users)

@app.route('/')
def index():
    return render_template('/users')

@app.route('/users')
def users():
    return render_template('read_all.html', all_friends=User.get_all())
    
    
@app.route('/new')
def new():
    return render_template('create.html')

@app.route('/user/create', methods=["POST"])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')
