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
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('read_all.html', all_friends=User.get_all())
    
    
@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/users/create', methods=["POST"])
def create():
    print(request.form)
    User.save(request.form)
    return redirect(f"/users/show/{request.form['id']}")

@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        "id":id
    }
    return render_template('edit.html', all_friends=User.get_one(data))

@app.route('/users/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template('show_user.html', all_friends=User.get_one(data))

@app.route('/users/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')
