from flask_app.config.mysqlconnection import connectToMySQL

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
        
    @classmethod
    def save_recipe(cls, data):
        query = """INSERT INTO recipes (name, description , instructions , date_cooked, under_30, created_at, updated_at)
                VALUES (%(name)s , %(description)s , %(instructions)s, %(date_cooked)s , %(under_30)s, NOW(), NOW());"""
                
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update_recipe(cls, data):
        query  = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_cooked=%(date_cooked)s, updated_at = NOW() WHERE id = %(id)s;"
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
    def delete_recipe(cls, data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)