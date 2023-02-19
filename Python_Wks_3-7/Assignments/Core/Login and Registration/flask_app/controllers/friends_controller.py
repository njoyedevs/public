from flask import render_template, request, redirect, session, flash

from flask_app.models import users, messages, friends

from flask_app import app, BCRYPT

@app.route('/delete/comment', methods=["POST"])
def delete_friend():
    
    data = {
        'id': request.form['id']
    }
    
    comments.Comment.delete_comment(data)
    return redirect('/dashboard')