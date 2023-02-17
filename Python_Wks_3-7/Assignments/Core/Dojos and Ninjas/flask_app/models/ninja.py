from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE

from flask import flash

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(DATABASE).query_db(query)
        
        ninjas = []
        
        for result in results:
            ninjas.append(result)
            
        return ninjas
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # print(results)
        return cls(results[0])
    
    @classmethod
    def save(cls,data):
        query = """INSERT INTO ninjas (first_name, last_name, 
                age, created_at, updated_at, dojo_id) Values
                (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"""
                
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # Other Ninja methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_ninja(ninjas):
        
        
        
        is_valid = True # we assume this is true
        if len(ninjas['first_name']) < 2:
            flash("First name must be at greater 2 characters.")
            is_valid = False
        if len(ninjas['last_name']) < 2:
            flash("Last name must be at greater 2 characters.")
            is_valid = False
        if int(ninjas['age']) > 9999999999:
            flash("Age must be less than 9999999999")
            is_valid = False
        return is_valid
    
    # @classmethod
    # def get_all_ninjas(cls):
    #     query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.user_id = dojos.id;"
        
    #     results = connectToMySQL(DATABASE).query_db(query)
        
    #     dojo = []
        
    #     for row in results:
    #         ninja = cls(row)
            
    #         ninja_data = {
    #             **row,
    #             'id': row['dojos.id'],
    #             'created_at': row['dojos.created_at'],
    #             'updated_at': row['dojos.updated_at']
    #         }

    #         ninja.owner = Ninja(ninja_data)
    #         dojo.append(ninja)
            
    #     return dojo