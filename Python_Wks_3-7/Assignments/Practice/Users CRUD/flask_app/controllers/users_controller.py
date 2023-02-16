from flask import render_template, request, redirect

from flask_app.models.users import User

from flask_app import app

# @app.route('/')
# def index():
#     users = User.get_all()
#     print(users)
#     return render_template("index.html", users = users)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('read_all.html', users=User.get_all())
    
@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/users/create', methods=["POST"])
def create():
    print(request.form)
    id = User.save(request.form)
    return redirect(f"/users/{id}")

@app.route('/users/<int:id>/edit')
def edit(id):
    data = {
        "id":id
    }
    return render_template('edit.html', users=User.get_one(data))

@app.route('/users/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template('show_user.html', users=User.get_one(data))

@app.route('/users/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/<int:id>/destroy/')
def delete(id):
    
    data = {
        'id': id
    }
    
    User.delete(data)
    return redirect('/')