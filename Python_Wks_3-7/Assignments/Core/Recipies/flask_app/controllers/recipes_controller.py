from flask import render_template, request, redirect, session, flash

from flask_app.models import recipes

from flask_app import app, BCRYPT

@app.route('/recipes')
def recipies():
    return render_template('recipes.html', recipes=recipes.Recipe.get_all_recipes())  

@app.route('/recipes/new')
def new_recipe():
    return render_template('create_recipe.html')

@app.route('/recipes/create', methods=["POST"])
def create_recipe():
    id = recipes.Recipe.save_recipe(request.form)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    data = {
        "id":id
    }
    return redirect('show_recipe.html', recipe=recipes.Recipe.get_one_recipe(data))

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    data = {
        "id":id
    }
    return render_template('edit_recipe.html', recipe=recipes.Recipe.get_one_recipe(data))

@app.route('/recipes/update', methods=["POST"])
def update_recipe():
    recipes.Recipe.update_recipe(request.form)
    return redirect('/recipes')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    
    data = {
        'id': id
    }
    
    recipes.Recipe.delete_recipe(data)
    return redirect('/recipes')