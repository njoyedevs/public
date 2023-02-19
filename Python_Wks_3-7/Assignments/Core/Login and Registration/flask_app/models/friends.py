from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE

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
    
    # @classmethod
    # def get_one_comment(cls,data):
    #     query = "SELECT * FROM comments WHERE id = %(id)s"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     return cls(results[0])
    
    @classmethod
    def get_all_friends(cls,data):
        print(data)
        query = "SELECT * FROM friends WHERE user_id = 1;"
        
        results = connectToMySQL(DATABASE).query_db(query, data)
        # print(results)
        # friends = []
        
        # for friend in results:
        #     friends.append( cls(friend) )
            
        # return friends
    
    # def get_friendship_info(cls,data):
    #     query = """SELECT * FROM users 
    #             LEFT JOIN friends ON
    #             friends.user_id = users.id
    #             LEFT JOIN users as users_2 ON
    #             friends.friend_id = users_2.id
    #             WHERE users.id = %(data)s;"""
        
    #     results = connectToMySQL(DATABASE).query_db(query, data)

    #     data_array = []
        
    #     for item in results:
    #         data_array.append( cls(item) )

    #     return data_array
    
    @classmethod
    def get_friendship_info(cls,data):
        
        print(data)
        
        # # query = "SELECT * FROM dojos LEFT JOIN ninjas on ninjas.dojo_id=dojos.id WHERE dojos.id = %(id)s;"  # Cant get this to work!
        query = f"""SELECT * FROM users 
                LEFT JOIN friends ON
                friends.user_id = users.id
                LEFT JOIN users AS users_2 ON
                friends.friend_id = users_2.id
                WHERE users.id = {data};"""
        
        results = connectToMySQL(DATABASE).query_db(query,data)
        
        print(results)
        
        # dojo = cls(results[0])
        
        # for ninja_in_dojo in results:
            
        #     ninja_data = {
        #         "id" : ninja_in_dojo['ninjas.id'],
        #         "first_name" : ninja_in_dojo['first_name'],
        #         "last_name" : ninja_in_dojo['last_name'],
        #         "age" : ninja_in_dojo['age'],
        #         "created_at" : ninja_in_dojo['ninjas.created_at'],
        #         "updated_at" : ninja_in_dojo['ninjas.updated_at']
        #     }
        
        #     dojo.ninjas.append(Ninja(ninja_data))
        
        # return dojo

    # @classmethod
    # def get_sent_comments(cls,data):
    #     query = "SELECT * FROM comments WHERE login_id = %(id)s"
    #     results = connectToMySQL(DATABASE).query_db(query, data)

    #     if results != False:
    #         messages = []
        
    #         for message in results:
    #             messages.append( cls(message) )

    #         return messages
    
    @classmethod
    def delete_friend(cls, data):
        query  = "DELETE FROM friends WHERE friend_id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    