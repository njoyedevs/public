from flask import render_template, request, redirect, session, flash

from flask_app.models import users, messages, friends

from flask_app import app, BCRYPT

@app.route('/friendships')
def friendships():
    
    user = users.User.get_one_user(session['user_id'])
    # print(user.first_name)
    
    users_list = users.User.get_all_users()
    # print(users_list)
    
    # friendships= friends.Friend.get_friendship_info(session['user_id'])
    friendships= friends.Friend.get_all_friends(session['user_id'])
    
    return render_template('friendships.html', one_user=user,all_users=users_list ) #friendship=friendships

@app.route('/create/friendship', methods=["POST"])
def create_friend():
    
    # print('Test')
    # print(request.form)
    
    data = {
        'user_id': request.form['user_id'],
        'friend_id': request.form['friend_id']
    }
    
    friends.Friend.save_friend(data)
    
    return redirect('/friendships')


@app.route('/delete/friendship', methods=["POST"])
def delete_friend():
    
    data = {
        'friend_id': request.form['friend_id']
    }
    
    friends.Friend.delete_friend(data)
    return redirect('/friendships')