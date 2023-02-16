# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # query = "SELECT * FROM friends WHERE id=1"
        # query = "UPDATE friends SET first_name='Bryanna' WHERE id=3"
        
        ############## Prepared Statements ######################
        # # Example when needing to develop prepared statements
        # query = "SELECT * FROM users WHERE email = %(email)s;"
        
        # # the placeholder variable is called email
        # # it must match the key name in the data dictionary
        # data = { 
        #     # this 'email' Key in data must be named to match the placeholder in the query.
        #     'email' : request.form['email'] 
        # }
        
        # results = connectToMySQL('first_flask').query_db(query, data)
        #########################################################
        
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        print(results)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
            
        return friends
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('first_flask').query_db( query, data )
    
    # the update method will be used when we need to update a friend in our database
    @classmethod
    def update(cls,data):
        query = """UPDATE friends 
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s 
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)
            
    # the delete method will be used when we need to delete a friend from our database
    @classmethod
    def delete(cls, friend_id):
        query  = "DELETE FROM friends WHERE id = %(id)s};"
        data = {"id": friend_id}
        return connectToMySQL(cls.DB).query_db(query, data)
