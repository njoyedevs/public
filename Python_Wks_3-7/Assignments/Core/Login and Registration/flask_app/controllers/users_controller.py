from flask import render_template, request, redirect, session, flash

from flask_app.models import users, messages, comments

from flask_app import app, BCRYPT

@app.route('/')
def index():
    # return redirect('/users')
    return render_template('index.html')   

@app.route('/dashboard')
def dashboard():
    
    if not 'user_id' in session:
        flash('Access Denied. Please log in first.')
        return redirect('/')
    
    id = session['user_id']
    
    outbox_messages = messages.Message.get_sent_messages(id)
    if outbox_messages != None:
        outbox_count = len(outbox_messages)
    else:
        outbox_count = 0
    
    inbox_messages = messages.Message.get_recieved_messages(id)
    if inbox_messages != None:
        inbox_count = len(inbox_messages)
    else:
        inbox_count = 0
    
    message_info = {
        'inbox_count': inbox_count,
        'outbox_count': outbox_count,
        # 'recipient_name': recipient_name,
        'inbox_messages': inbox_messages,
        'outbox_messages': outbox_messages,
    }
    
    return render_template('secure.html', all_users=users.User.get_all_users(), one_user=users.User.get_one_user(id), messages=message_info)   #messages=message_info,  user=logins.User.get_one_user(id),

@app.route('/send', methods=["POST"])
def send_message():
    
    data = {
        'user_id': request.form['user_id'],
        "recipient_id": request.form['recipient_id'],
        "message": request.form['message_box'],
    }
    
    if not messages.Message.check_text(request.form):
        return redirect('/dashboard')
    
    messages.Message.save_message(data)
    
    return redirect('/dashboard')

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

@app.route('/delete/user', methods=["POST"])
def delete_user():
    
    data = {
        'id': request.form['id']
    }
    
    users.User.delete_user(data)
    session.clear()
    return redirect('/')

@app.route('/delete/message', methods=["POST"])
def delete_message():
    
    data = {
        'id': request.form['recipient_id']
    }
    
    messages.Message.delete_message(data)
    return redirect('/dashboard')

@app.route('/delete/comment', methods=["POST"])
def delete_comment():
    
    data = {
        'id': request.form['id']
    }
    
    comments.Comment.delete_comment(data)
    return redirect('/dashboard')

