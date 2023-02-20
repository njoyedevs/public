from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE, BCRYPT

from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r"(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$")

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.optimism = data['optimism']
        self.password = data['password']
        self.confirm = data['confirm']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save_user(cls, data):
        query = """INSERT INTO users (first_name , last_name , email, optimism, password, confirm, created_at, updated_at)
                VALUES (%(first_name)s , %(last_name)s , %(email)s, %(optimism)s , %(password)s , %(confirm)s, NOW(), NOW());"""
                
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_one_user(cls,data):
        query = f"SELECT * FROM users WHERE id = {data}" #### Can't get this to work add %(id)s when fixed
        
        results = connectToMySQL(DATABASE).query_db(query) ### Add , data when fixed
        # print(results)
        return cls(results[0])
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        logins = []
        
        for login in results:
            logins.append( cls(login) )
            
        return logins
    
    @classmethod
    def update(cls, data):
        query  = "UPDATE users SET first_name  = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('Users').query_db(query, data)
    
    # @classmethod
    # def get_one(cls,data):
    #     query = "SELECT * FROM users WHERE id = %(id)s"
    #     results = connectToMySQL('Users').query_db(query, data)
    #     return cls(results[0])
    
    @classmethod
    def delete(cls, data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('Users').query_db(query, data)
    
    @classmethod
    def verify_one(cls,data):
        
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        
        return results
    
    @classmethod
    def email_used(cls, data):
        
        query = "SELECT email FROM users WHERE email = %(email)s"
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        
        is_valid = False
        
        if len(results) > 0:
            is_valid = True
            
        return is_valid
    
    @staticmethod
    def validate_name(data):
        
        names = ['first_name', 'last_name']
        
        is_valid = True
        
        for name in names:
        
            if(re.match("^[a-zA-Z]*$", data[name]) == None):
                flash("First/Last name may only be alpha characters!", 'naming_error')
                is_valid = False
                
            if len(data[name]) < 2:
                flash("First/Last name must be at least 2 characters!", 'naming_error')
                is_valid = False
                
        return is_valid
    
    @staticmethod
    def check_email(data):

        is_valid = True
        data_dict = {
            'email': f"{data['email']}"
        }

        if User.email_used(data_dict):
            flash("Emailed Already Used!", 'email_error')
            is_valid = False
            
        return is_valid
    
    @staticmethod
    def is_email(data):
        
        is_valid = True
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", 'email_error')
            is_valid = False
            
        return is_valid

    @staticmethod
    def compare_password(data):
        
        is_valid = True
        if data['password'] != data['confirm']:
            flash(u"Passwords do not match!", 'password_error')
            is_valid = False
            
        res = re.search(PASSWORD_REGEX, data['password'])
            
        if not res:
            flash("""Passwords must be at least 8 characters and
                contain: 1(A-Z),1(a-z),1(0-9),1(!@#$%^&*)""", 'password_error')
            is_valid = False
        
        return is_valid
