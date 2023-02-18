from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE

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
        query = """INSERT INTO messages (recipient_id , message , read, created_at, updated_at)
                VALUES (%(recipient_id)s , %(message)s , %(read)s, NOW(), NOW());"""
                
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # @classmethod
    # def update(cls, data):
    #     query  = "UPDATE users SET first_name  = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_one_message(cls,data):
        print(data)
        query = "SELECT * FROM messages WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
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
        query = "SELECT * FROM messages WHERE recipient_id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if results != False:
            messages = []
        
            for message in results:
                messages.append( cls(message) )

            return messages

    @classmethod
    def get_sent_messages(cls,data):
        query = "SELECT * FROM messages WHERE login_id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if results != False:
            messages = []
        
            for message in results:
                messages.append( cls(message) )

            return messages
    
    # @classmethod
    # def get_user_comt_mesg(cls,data):
    #     query = """SELECT * FROM logins.logins 
    #             LEFT JOIN logins.comments ON
    #             logins.comments.login_id = logins.logins.id
    #             LEFT JOIN logins.messages ON
    #             logins.messages.login_id = logins.logins.id
    #             WHERE logins.logins.id = %(id)s;"""
        
    #     results = connectToMySQL(DATABASE).query_db(query, data)

    #     data_array = []
        
    #     for item in results:
    #         data_array.append( item )

    #     return data_array
    
    @classmethod
    def delete_message(cls, data):
        query  = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    