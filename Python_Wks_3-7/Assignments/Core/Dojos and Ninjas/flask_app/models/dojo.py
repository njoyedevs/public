from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def save(cls,data):
        query = """INSERT INTO dojos (name, created_at, updated_at)
                Values (%(name)s, NOW(), NOW())"""
                
        return connectToMySQL('dojos').query_db(query,data)
    
    @classmethod
    def get_all():
        query = 'SELECT * FROM dojos'
        results = connectToMySQL('dojos').query_db(query)
        
        dojos = []
        
        for result in results:
            dojos.append(result)
            
        return dojos
        
        
    
