from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE

class Friend:
    def __init__(self,data):
        self.id = data['id']
        self.friend_id = data['friend_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save_comment(cls, data):
        query = """INSERT INTO comments (comment, created_at, updated_at)
                VALUES (%(comment)s , NOW(), NOW());"""
                
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_one_comment(cls,data):
        query = "SELECT * FROM comments WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_all_comments(cls):
        query = "SELECT * FROM comments;"
        
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        comments = []
        
        for comment in results:
            comments.append( cls(comment) )
            
        return comments

    @classmethod
    def get_sent_comments(cls,data):
        query = "SELECT * FROM comments WHERE login_id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if results != False:
            messages = []
        
            for message in results:
                messages.append( cls(message) )

            return messages
    
    @classmethod
    def delete_comment(cls, data):
        query  = "DELETE FROM comments WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    