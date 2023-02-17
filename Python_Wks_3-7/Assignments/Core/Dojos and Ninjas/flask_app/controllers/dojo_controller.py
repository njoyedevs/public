from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo

from flask_app import app


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    return render_template('dojo.html', dojos=Dojo.get_all())

@app.route('/dojos/<int:id>')
def dojosShow(id):
    data = {
        "id":id
    }
    return render_template('dojo_show.html', dojo=Dojo.get_dojo_with_ninjas(data))

@app.route('/dojos/create', methods=["POST"])
def dojoCreate():
    Dojo.save(request.form)
    return redirect('/dojos')

