from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import users

from flask_app import DATABASE, BCRYPT

from flask import flash

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipe_list = []
        
    @classmethod
    def save_recipe(cls, data):
        query = """INSERT INTO recipes (name, description , instructions , date_cooked, under_30, created_at, updated_at, user_id)
                VALUES (%(name)s , %(description)s , %(instructions)s, %(date_cooked)s , %(under_30)s, NOW(), NOW(), %(user_id)s);"""
                
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update_recipe(cls, data):
        print(data)
        query  = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_cooked=%(date_cooked)s, under_30=%(under_30)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    @classmethod
    def get_one_recipe(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        
        results = connectToMySQL(DATABASE).query_db(query)
 
        recipes = []
        
        for recipe in results:
            recipes.append( cls(recipe) )
            
        return recipes
    
    @classmethod
    def get_all_recipes_for_user(cls,data):
        
        query = f"SELECT * FROM recipes LEFT JOIN users on recipes.user_id=users.id WHERE users.id = {data};"
        
        results = connectToMySQL(DATABASE).query_db(query,data)
        
        # print(results)
        
        recipes = cls(results[0])
        
        for recipe_for_user in results:
            
            user_data = {
                "id" : recipe_for_user['users.id'],
                "first_name" : recipe_for_user['first_name'],
                "last_name" : recipe_for_user['last_name'],
                "email" : recipe_for_user['m'],
                "created_at" : recipe_for_user['users.created_at'],
                "updated_at" : recipe_for_user['users.updated_at']
            }
        
            recipes.recipe_list.append(users.User(user_data))
        
        print(recipes)
        
        return recipes
                
    @classmethod
    def delete_recipe(cls, data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)