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
        query = """INSERT INTO messages (user_id, recipient_id , message , created_at, updated_at)
                VALUES (%(user_id)s , %(recipient_id)s , %(message)s , NOW(), NOW());"""
        
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
    def get_sent_messages(cls,data):

        query = "SELECT * FROM messages LEFT JOIN users ON users.id = messages.user_id WHERE user_id = '1'" #### Can't get this to work add %(id)s when fixed
        results = connectToMySQL(DATABASE).query_db(query) ### Add , data when fixed
        print(results)

        # if results != False:
        #     messages = []
        
        #     for message in results:
        #         messages.append( cls(message) )

        #     return messages
        
        
    
    @classmethod
    def get_recieved_messages(cls,data):
        
        query = "SELECT * FROM messages LEFT JOIN users ON users.id = messages.user_id WHERE recipient_id = '1'" #### Can't get this to work add %(id)s when fixed
        results = connectToMySQL(DATABASE).query_db(query) ### Add , data when fixed
        print(results)

        if results != False:
            messages = []
        
            for message in results:
                messages.append( cls(message) )

            return messages

    @classmethod
    def delete_message(cls, data):
        query  = "DELETE FROM messages WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    