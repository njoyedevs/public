from flask_app.config.mysqlconnection import connectToMySQL

# from flask_app.models.dojo import Dojo

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def save(cls,data):
        query = """INSERT INTO ninjas (id, first_name, last_name, 
                age, created_at, updated_at) Values
                (%(id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"""
                
        return connectToMySQL('ninjas').query_db(query,data)
    
    @classmethod
    def get_all():
        query = 'SELECT * FROM ninjas'
        results = connectToMySQL('ninjas').query_db(query)
        
        ninjas = []
        
        for result in results:
            ninjas.append(result)
            
        return ninjas
    
    # @classmethod
    # def get_all_ninjas(cls):
    #     query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.user_id = dojos.id;"
        
    #     results = connectToMySQL('ninjas').query_db(query)
        
    #     dojo = []
        
    #     for row in results:
    #         ninja = cls(row)
            
    #         ninja_data = {
    #             **row,
    #             'id': row['dojos.id'],
    #             'created_at': row['dojos.created_at'],
    #             'updated_at': row['dojos.updated_at']
    #         }

    #         ninja.owner = Ninja(ninja_data)
    #         dojo.append(ninja)
            
    #     return dojo