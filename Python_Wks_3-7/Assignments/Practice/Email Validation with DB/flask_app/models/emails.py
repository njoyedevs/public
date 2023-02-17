from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE

from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        print("initiated")
        
    @classmethod
    def save(cls,data):
        query = """INSERT INTO emails (email, created_at, updated_at) Values
                (%(email)s, NOW(), NOW());"""
        
        print("Saved")   
        return connectToMySQL(DATABASE).query_db(query,data)
    
    def get_all(cls):
        query = 'SELECT * FROM emails;'
        
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        emails = []
        
        for email in results:
            emails.append(email)
            
        return emails
    
    @staticmethod
    def validate_user(data):
        
        is_valid = True # we assume this is true
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False
            
        print("Validated")
        return is_valid