from flask import render_template, request, redirect, session, flash

from flask_app.models import users

from flask_app import app, BCRYPT

# @app.route('/')
# def index():
#     users = User.get_all()
#     print(users)
#     return render_template("index.html", users = users)

@app.route('/')
def index():
    # return redirect('/users')
    return render_template('index.html')  

@app.route('/registration', methods=["POST"])
def create():

    
    if not users.User.validate_name(request.form):
        return redirect('/')

    if not users.User.is_email(request.form):
        return redirect('/')
    
    if not users.User.check_email(request.form):
        return redirect('/')
    
    if not users.User.compare_password(request.form):
        return redirect('/')
    
    pw_hash = BCRYPT.generate_password_hash(request.form['password'])
    
    cnf_hash = BCRYPT.generate_password_hash(request.form['confirm'])

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        'optimism': request.form['optimism'],
        "password":pw_hash,
        "confirm": cnf_hash,
    }
    
    user_id = users.User.save_user(data)
    
    session['user_id'] = user_id
    
    return redirect('/dashboard')

@app.route('/login', methods=["POST"])
def login():
    
    user_data = users.User.verify_one(request.form)
    
    if not user_data:
        flash('User does not exist', 'login_error')
        return redirect('/')

    if not BCRYPT.check_password_hash(user_data[0]['password'], request.form['password']):
        # if we get False after checking the password
        flash("Invalid Password", 'password_error')
        return redirect('/')
    
    session['user_id'] = user_data[0]['id']
    
    return redirect('/dashboard')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')

# @app.route('/users')
# def users():
#     return render_template('read_all.html', users=users.User.get_all())
    
# @app.route('/users/new')
# def new():
#     return render_template('create.html')

# @app.route('/users/create', methods=["POST"])
# def create():
#     print(request.form)
#     id = users.User.save(request.form)
#     return redirect(f"/users/{id}")

# @app.route('/users/<int:id>/edit')
# def edit(id):
#     data = {
#         "id":id
#     }
#     return render_template('edit.html', users=users.User.get_one(data))

# @app.route('/users/<int:id>')
# def show(id):
#     data = {
#         "id":id
#     }
#     return render_template('show_user.html', users=users.User.get_one(data))

# @app.route('/users/update', methods=["POST"])
# def update():
#     users.User.update(request.form)
#     return redirect('/users')

# @app.route('/users/<int:id>/destroy/')
# def delete(id):
    
#     data = {
#         'id': id
#     }
    
#     users.User.delete(data)
#     return redirect('/')