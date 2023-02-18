from flask import render_template, request, redirect, session, flash

from flask_app.models.logins import User

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

@app.route('/dashboard')
def dashboard():
    # return redirect('/users')
    return render_template('dashboard.html', data=User.get_all())   

# @app.route('/users')
# def users():
#     return render_template('read_all.html', users=User.get_all())
    
    
# @app.route('/users/new')
# def new():
#     return render_template('create.html')

@app.route('/registration', methods=["POST"])
def create():
    
    if not User.validate_name(request.form):
        return redirect('/')

    if not User.is_email(request.form):
        return redirect('/')
    
    if not User.check_email(request.form):
        return redirect('/')
    
    if not User.compare_password(request.form):
        return redirect('/')
    
    pw_hash = BCRYPT.generate_password_hash(request.form['password'])
    
    cnf_hash = BCRYPT.generate_password_hash(request.form['confirm'])

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password":pw_hash,
        "confirm": cnf_hash,
    }
    
    user_id = User.save(data)
    
    session['user_id'] = user_id
    
    return redirect('/dashboard')

@app.route('/login', methods=["POST"])
def login():
    print(request.form)
    
    # if not User.check_email(request.form):
    #     return redirect('/')
    
    user_data = User.verify_one(request.form)
    print(user_data)
    
    if not user_data:
        flash('User does not exist', 'login_error')
        return redirect('/')

    if not BCRYPT.check_password_hash(user_data[0]['password'], request.form['password']):
        # if we get False after checking the password
        flash("Invalid Password", 'password_error')
        return redirect('/')
    
    session['user_id'] = user_data[0]['id']
    
    return redirect('/dashboard')

# @app.route('/users/<int:id>/edit')
# def edit(id):
#     data = {
#         "id":id
#     }
#     return render_template('edit.html', users=User.get_one(data))

# @app.route('/users/<int:id>')
# def show(id):
#     data = {
#         "id":id
#     }
#     return render_template('show_user.html', users=User.get_one(data))

# @app.route('/users/update', methods=["POST"])
# def update():
#     User.update(request.form)
#     return redirect('/users')

# @app.route('/users/<int:id>/destroy/')
# def delete(id):
    
#     data = {
#         'id': id
#     }
    
#     User.delete(data)
#     return redirect('/')