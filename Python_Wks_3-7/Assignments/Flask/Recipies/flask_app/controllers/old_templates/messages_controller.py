from flask import render_template, request, redirect, session, flash

from flask_app.models import users, messages, friends

from flask_app import app, BCRYPT


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

@app.route('/message', methods=["POST"])
def friend_message():
    
    data = {
        "recipient_id": request.form['recipient_id'],
        "message": request.form['message_box'],
        'read': False,
        'user_id': session['user_id']
    }
    
    if not messages.Message.check_text(request.form):
        return redirect('/friendships')
    
    messages.Message.save_message(data)
    
    return redirect('/friendships')

@app.route('/delete/message', methods=["POST"])
def delete_message():
    
    data = {
        'id': request.form['recipient_id']
    }
    
    messages.Message.delete_message(data)
    return redirect('/dashboard')