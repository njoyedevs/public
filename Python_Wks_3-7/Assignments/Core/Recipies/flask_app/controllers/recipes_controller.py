from flask import render_template, request, redirect, session, flash

from flask_app.models import recipes

from flask_app import app, BCRYPT

@app.route('/recipes')
def recipies():
    
    return render_template('recipes.html',recipes=recipes.Recipe.get_all_recipes_for_user({'id':session['user_id']}))

@app.route('/recipes/dashboard')
def dashboard():
    
    #recipes.Recipe.get_all_recipes_for_all_users()
    
    return render_template('all_recipes.html',recipes=recipes.Recipe.get_all_recipes_for_user({'id':session['user_id']})) # recipes=recipes.Recipe.get_all_recipes_for_all_users()

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
    
    return render_template('show_recipe.html', recipe=recipes.Recipe.get_user_for_recipe(data))

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    
    session['recipe_id'] = id
    # print(id)
    
    data = {
        "id":id
    }
    
    return render_template('edit_recipe.html', recipe=recipes.Recipe.get_one_recipe(data))

@app.route('/recipes/update', methods=["POST"])
def update_recipe():
    
    # print(request.form)
    # print(session['recipe_id'] )
    
    if request.form['date_cooked']  == '':
        flash(u"Please select a date!", 'edit_error')
        return redirect(f'/recipes/edit/{session["recipe_id"]}')
    
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_cooked': request.form['date_cooked'],
        'under_30': request.form['under_30'],
        'user_id': session['user_id'],
        'id': request.form['recipe_id']
    }
    
    last_row_id = recipes.Recipe.update_recipe(data)
    # print(last_row_id)
    return redirect('/recipes')

@app.route('/recipes/delete/<int:id>')
def delete_recipe(id):
    
    data = {
        'id': id
    }
    
    recipes.Recipe.delete_recipe(data)
    return redirect('/recipes')