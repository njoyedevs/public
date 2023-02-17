from flask import render_template, redirect, request

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

from flask_app import app

@app.route('/ninjas')
def ninja():
    return render_template('ninja.html', dojos=Dojo.get_all())

@app.route('/ninjas/<int:id>')
def ninjaShow(id):
    data = {
        "id":id
    }
    return render_template('ninja_show.html', ninja=Ninja.get_one(data))

@app.route('/ninja/create', methods=["POST"])
def ninjaCreate():
    # print(request.form)
    
    if not Ninja.validate_ninja(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/ninjas')
    # else no errors:
    id = Ninja.save(request.form)
    
    return redirect(f"/dojos/{request.form['dojo_id']}")