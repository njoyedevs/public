from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

from flask_app import app

@app.route('/')
def index():
    return render_template('index.html', ninjas=Ninja.get_all(), dojos=Dojo.get_all())