from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE

from flask_app.models import users

import re

from flask import flash

import math

from datetime import datetime

class Message:
    def __init__(self,data):
        self.id = data['id']
        self.recipient_id = data['recipient_id']
        self.message = data['message']
        self.read = data['read']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save_message(cls, data):
        query = """INSERT INTO messages (user_id, recipient_id , message , created_at, updated_at)
                VALUES (%(user_id)s , %(recipient_id)s , %(message)s , NOW(), NOW());"""
        # print(query)
        
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_one_message(cls,data):
        query = "SELECT * FROM messages WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_all_messages(cls):
        query = "SELECT * FROM messages;"
        
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        messages = []
        
        for message in results:
            messages.append( cls(message) )
            
        return messages
    
    @classmethod
    def get_recieved_messages(cls,data):
        
        # print(data)
        
        # # Fetch the user to associate with all the message objects
        #sender = users.User.get_one_user(data)

        query = f"""SELECT messages.*, first_name, last_name, email, optimism, password, confirm, recipient.created_at as recipient_created_at, recipient.updated_at as recipient_updated_at
                FROM messages
                JOIN users as recipient ON messages.user_id = recipient.id
                WHERE recipient_id =  {data}"""
        results = connectToMySQL(DATABASE).query_db(query)
        # print(f'THIS IS RECIEVED: {results}')

        # Create and populate a list of message objects
        messages = []

        for message in results:
            # # Make the sender object
            # recipient_data = {
            #     "id": message["user_id"],
            #     "first_name": message["first_name"],
            #     "last_name": message["last_name"],
            #     "email": message["email"],
            #     'optimism': message["optimism"],
            #     'password': message["password"],
            #     'confirm': message["confirm"],
            #     "created_at": message["recipient_created_at"],
            #     "updated_at": message["recipient_updated_at"],
            # }
            # recipient = users.User(recipient_data)
            # print(message['user_id'])
            sender = users.User.get_one_user(message['user_id'])
            # print(sender.first_name)

            # Make the message object
            message = {
                "id": message["id"],
                'recipient_id': message['recipient_id'],
                "message": message["message"],
                'read': message['read'],
                "created_at": message["created_at"],
                "updated_at": message["updated_at"],
            }
            messages.append( [cls(message), sender.first_name])
            
        # print(messages)

        return messages
    
    @classmethod
    def get_sent_messages(cls,data):
        
        # # Fetch the user to associate with all the message objects
        # recipient = users.User.get_one_user(data)

        query = f"""SELECT messages.*, first_name, last_name, email, optimism, password, confirm, senders.created_at as sender_created_at, senders.updated_at as sender_updated_at
                FROM messages
                JOIN users as senders ON messages.user_id = senders.id
                WHERE user_id =  {data}"""
        results = connectToMySQL(DATABASE).query_db(query)
        # print(f'THIS IS RECIEVED: {results}')

        # Create and populate a list of message objects
        messages = []

        for message in results:
            # # Make the sender object
            # sender_data = {
            #     "id": message["user_id"],
            #     "first_name": message["first_name"],
            #     "last_name": message["last_name"],
            #     "email": message["email"],
            #     'optimism': message["optimism"],
            #     'password': message["password"],
            #     'confirm': message["confirm"],
            #     "created_at": message["sender_created_at"],
            #     "updated_at": message["sender_updated_at"],
            # }
            # sender = users.User(sender_data)

            # Make the message object
            message = {
                "id": message["id"],
                'recipient_id': message['recipient_id'],
                "message": message["message"],
                'read': message['read'],
                "created_at": message["created_at"],
                "updated_at": message["updated_at"],
            }
            messages.append( cls(message) )

        return messages

    @classmethod
    def delete_message(cls, data):
        
        print(data)
        
        query  = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def check_text(data):  # COUND NOT GET THIS TO WORK
        
        is_valid = True
        # if not TEXT_REGEX.match(data['message_box']):
        #     flash("Messages must have 5 characters!", 'text_error')
        #     is_valid = False
            
        return is_valid
    
    @classmethod
    def time_span(self,data):
        now = datetime.now()
        delta = now - data
        # print(delta.days)
        # print(delta.total_seconds())
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"
        
        
    # @classmethod
    # def get_sent_messages(cls,data):

    #     query = f"SELECT * FROM messages LEFT JOIN users ON users.id = messages.user_id WHERE user_id = {data}" #### Can't get this to work add %(id)s when fixed

    #     results = connectToMySQL(DATABASE).query_db(query) ### Add , data when fixed
    #     print(results)

    #     if results != False:
    #         messages = []
        
    #         for message in results:
    #             messages.append( cls(message) )

    #         return messages
        
    # @classmethod
    # def get_recieved_messages(cls,data):
        
    #     query = f"SELECT * FROM messages LEFT JOIN users ON users.id = messages.user_id WHERE recipient_id = {data}" #### Can't get this to work add %(id)s when fixed
    #     results = connectToMySQL(DATABASE).query_db(query) ### Add , data when fixed
    #     # print(results)

    #     if results != False:
    #         messages = []
        
    #         for message in results:
    #             messages.append( cls(message) )

    #         return messages
    