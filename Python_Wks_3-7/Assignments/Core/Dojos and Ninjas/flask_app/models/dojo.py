from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        
        results = connectToMySQL('Dojos_and_Ninjas').query_db(query)
        print(results)
        dojos = []
        
        for dojo in results:
            dojos.append(dojo)
            
        return dojos
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL('Dojos_and_Ninjas').query_db(query, data)
        print(results)
        return cls(results[0])
    
    @classmethod
    def save(cls,data):
        query = """INSERT INTO dojos (name, created_at, updated_at)
                Values (%(name)s, NOW(), NOW())"""
                
        return connectToMySQL('Dojos_and_Ninjas').query_db(query,data)
    
    @classmethod
    def get_dojo_with_ninjas(cls,data):
        
        query = "SELECT * FROM dojos LEFT JOIN ninjas on ninjas.dojo_id=dojos.id WHERE dojos.id = %(id)s;"
        
        results = connectToMySQL('Dojos_and_Ninjas').query_db(query,data)
        
        print(results)
        
        dojo = cls(results[0])
        
        for ninja_in_dojo in results:
            
            ninja_data = {
                "id" : ninja_in_dojo['ninjas.id'],
                "first_name" : ninja_in_dojo['first_name'],
                "last_name" : ninja_in_dojo['last_name'],
                "age" : ninja_in_dojo['age'],
                "created_at" : ninja_in_dojo['ninjas.created_at'],
                "updated_at" : ninja_in_dojo['ninjas.updated_at']
            }
        
            dojo.ninjas.append(Ninja(ninja_data))
        
        return dojo
            
        
    
