from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import users

from flask_app import DATABASE, BCRYPT

from flask import flash

import datetime

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
        self.user_id = data['user_id']
        self.recipe_list = []
        
    @classmethod
    def save_recipe(cls, data):
        query = """INSERT INTO recipes (name, description , instructions , date_cooked, under_30, created_at, updated_at, user_id)
                VALUES (%(name)s , %(description)s , %(instructions)s, %(date_cooked)s , %(under_30)s, NOW(), NOW(), %(user_id)s);"""
                
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def update_recipe(cls, data):
        # print(data)
        query  = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_cooked=%(date_cooked)s, under_30=%(under_30)s, user_id=%(user_id)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
        
    @classmethod
    def get_one_recipe(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # print(results)
        
        return cls(results[0])
    
    @classmethod 
    def get_user_for_recipe(cls, data):
        
        query = "SELECT * FROM recipes LEFT JOIN users on recipes.user_id=users.id WHERE recipes.id = %(id)s;"
        
        results = connectToMySQL(DATABASE).query_db(query,data)

        print(results[0]['created_at'])
        date = results[0]['created_at']
        
        results[0]['created_at'] = cls.convert_date(date)
        print(results[0]['created_at'])
        recipes = []
        
        for row in results:
            
            recipe = cls(row)
            
            user_data = {
                **row,
                "id" : row['users.id'],
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at']
            }
        
            # print(f'Row: {row}')
            print(f'User Data: {user_data}')

            recipe.user = users.User(user_data)
            recipes.append(recipe)
        
        # print(recipes[0].created_at)
        
        return recipes[0]
    
    @staticmethod
    def convert_date(data):
        
        # create the datetime object
        dt = datetime.datetime(2023, 2, 19, 20, 4, 2)

        # convert to the desired string format
        dt_str = data.strftime('%m/%d/%Y %H:%M:%S')

        # print the result
        print(dt_str)  # outputs: "02/19/2023 20:04:02"
        return dt_str
    
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
        
        query = "SELECT * FROM recipes LEFT JOIN users on recipes.user_id=users.id WHERE users.id = %(id)s;"
        
        results = connectToMySQL(DATABASE).query_db(query,data)
        
        # print(results)
        
        recipes = []
        
        for row in results:
            
            recipe = cls(row)
            
            user_data = {
                **row,
                "id" : row['users.id'],
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at']
            }
        
            # print(f'Row: {row}')
            # print(f'User Data: {user_data}')

            recipe.user = users.User(user_data)
            recipes.append(recipe)
        
        # print(recipes)
        
        return recipes
    
    @classmethod
    def get_all_recipes_for_all_users(cls):
        
        query = "SELECT * FROM recipes LEFT JOIN users on recipes.user_id=users.id WHERE recipes.id"
                
        # print(query)
        
        results = connectToMySQL(DATABASE).query_db(query)
        
        # print(results)
        
        recipes = []
        
        for row in results:
            
            recipe = cls(row)
            
            user_data = {
                **row,
                "id" : row['users.id'],
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at']
            }
        
            # print(f'Row: {row}')
            # print(f'User Data: {user_data}')

            recipe.user = users.User(user_data)
            recipes.append(recipe)
        
        # print(recipes)
        
        return recipes
        
        
    
    @classmethod
    def delete_recipe(cls, data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)