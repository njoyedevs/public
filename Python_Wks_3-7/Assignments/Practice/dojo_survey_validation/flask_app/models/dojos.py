from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE

from flask import flash

class User:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninja = []
        
    @classmethod
    def save(cls,data):
        query = """INSERT INTO dojos (name, location, 
                language, comment, created_at, updated_at) Values
                (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"""
                
        return connectToMySQL(DATABASE).query_db(query,data)
        
    @classmethod
    def get_recent(cls):
        query = "SELECT * FROM dojos ORDER BY id DESC LIMIT 1;"
        
        results = connectToMySQL(DATABASE).query_db(query)
        
        return cls(results[0])
    
    @staticmethod
    def validate_ninja(data):
        
        is_valid = True # we assume this is true
        if len(data['name']) < 2:
            flash("Name must be greater than 2 characters.")
            is_valid = False
        if len(data['location']) < 4:
            flash("Location must be greater than 4 characters.")
            is_valid = False
        if len(data['language']) < 4:
            flash("Language must be greater than 4 characters.")
            is_valid = False
            
            
        print("Validated")
        return is_valid