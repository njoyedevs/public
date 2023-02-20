from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE

from flask_app.models import users

from flask import flash

class Friend:
    def __init__(self,data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save_friend(cls, data):
        query = """INSERT INTO friends (created_at, updated_at, user_id, friend_id)
                VALUES (NOW(), NOW(), %(user_id)s, %(friend_id)s);"""
                
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_friendship_info(cls,data):
        
        # print(data)
        
        query = """SELECT * FROM users 
                LEFT JOIN friends ON
                friends.user_id = users.id
                LEFT JOIN users AS users_2 ON
                friends.friend_id = users_2.id
                WHERE users.id = %(id)s;"""
        
        results = connectToMySQL(DATABASE).query_db(query,data)
        
        # print(results)
        
        # user = cls(results[0])
        
        users_friends = []
        
        for row in results:
            
            friend = cls(row)
            
            friend_data = {
                **row,
                "id" : row['friends.id'],
                "created_at" : row['friends.created_at'],
                "updated_at" : row['friends.updated_at'],
                "id" : row['users_2.id'],
                "first_name" : row['users_2.first_name'],
                "last_name" : row['users_2.last_name'],
                "email" : row['users_2.email'],
                "optimism" : row['users_2.optimism'],
                "password" : row['users_2.password'],
                "confirm" : row['users_2.confirm'],
                "created_at" : row['users_2.created_at'],
                "updated_at" : row['users_2.updated_at']
            }
        
            # print(f'Row: {row}')
            # print(f'User Data: {friend_data}')

            friend.user2 = users.User(friend_data)
            users_friends.append(friend)
        
        # print(users_friends)
    
        return users_friends
    
    @classmethod
    def delete_friend(cls, data):
        query  = "DELETE FROM friends WHERE friend_id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    