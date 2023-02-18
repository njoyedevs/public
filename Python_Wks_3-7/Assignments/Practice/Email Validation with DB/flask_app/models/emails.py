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
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM emails;'
        
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        emails = []
        
        for email in results:
            emails.append(email)
            
        return emails
    
    @classmethod
    def get_recent(cls):
        query = "SELECT * FROM emails ORDER BY id DESC LIMIT 1;"
        
        results = connectToMySQL(DATABASE).query_db(query)
        
        if len(results) == 0:
            return False
        else:
            return cls(results[0])
        
    @classmethod
    def email_used(cls, data):
        query = "SELECT email FROM emails WHERE email = %(email)s"
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        
        is_valid = False
        
        if len(results) > 0:
            is_valid = True
            
        return is_valid
        
    @staticmethod
    def validate_user(data):
        
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False
            
        data_dict = {
            'email': f"{data['email']}"
        }

        if User.email_used(data_dict):
            flash("Emailed Already Used!")
            is_valid = False
            
        return is_valid
    
    @classmethod
    def delete(cls, data):
        print(data)
        query  = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)