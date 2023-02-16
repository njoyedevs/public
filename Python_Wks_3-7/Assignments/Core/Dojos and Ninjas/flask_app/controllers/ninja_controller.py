from flask_app.models.ninja import Ninja

from flask_app import app

from flask import render_template, redirect, request



# @app.route('/ninjas')
# def ninjas():
    
#     ninjas = Ninja.get_all_ninjas()
    
#     return render_template('ninjas.html', ninjas=ninjas)