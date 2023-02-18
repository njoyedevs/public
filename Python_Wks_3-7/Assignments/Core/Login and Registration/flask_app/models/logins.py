from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app, DATABASE, BCRYPT

from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PASSWORD_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$")
PASSWORD_REGEX = re.compile(r"(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$")
                            
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.confirm = data['confirm']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM logins;"
        
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     print(results)
    #     logins = []
        
    #     for login in results:
    #         logins.append( cls(login) )
            
    #     return logins
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO logins (first_name , last_name , email, password, confirm)
                VALUES (%(first_name)s , %(last_name)s , %(email)s , %(password)s , %(confirm)s);"""
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # @classmethod
    # def update(cls, data):
    #     query  = "UPDATE users SET first_name  = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)
    
    # @classmethod
    # def get_one(cls,data):
    #     query = "SELECT * FROM users WHERE id = %(id)s"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     return cls(results[0])
    
    # @classmethod
    # def delete(cls, data):
    #     query  = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def email_used(cls, data):
        query = "SELECT email FROM emails WHERE email = %(email)s"
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        
        is_valid = False
        
        if len(results) > 0:
            is_valid = True
            
        return is_valid
    
    @staticmethod
    def validate_email(data):
    
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", 'message_1')
            is_valid = False
            
        data_dict = {
            'email': f"{data['email']}"
        }

        if User.email_used(data_dict):
            flash("Emailed Already Used!", 'message_1')
            is_valid = False
            
        return is_valid

    @staticmethod
    def compare_password(data):
        
        is_valid = True
        if data['password'] != data['confirm']:
            flash("Passwords do not match!", 'message_1')
            is_valid = False
            
        res = re.search(PASSWORD_REGEX, data['password'])
            
        if not res:
            flash("""Passwords must be at least 8 characters and
                contain: 1(A-Z),1(a-z),1(0-9),1(!@#$%^&*)""", 'message_1')
            is_valid = False
        
        return is_valid