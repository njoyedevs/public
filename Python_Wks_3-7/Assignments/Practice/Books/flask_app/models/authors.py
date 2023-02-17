from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import books

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM authors;'
        
        results = connectToMySQL('Books_ERD').query_db(query)
        print(results)
        authors = []
        
        for book in results:
            authors.append(book)
            
        return authors
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM authors WHERE id = %(id)s"
        results = connectToMySQL('Books_ERD').query_db(query, data)
        print(results)
        return cls(results[0])
    
    @classmethod
    def save(cls,data):
        query = """INSERT INTO authors (name, created_at, updated_at, book_id)
                Values (%(name)s, NOW(), NOW(), %(book_id)s )"""
                
        return connectToMySQL('Books_ERD').query_db(query,data)
    
    @classmethod
    def get_authors_fav_books(cls,data):
        
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id=authors.id LEFT JOIN books ON favorites.book_id=books.id WHERE authors.id = %(id)s;"
        
        results = connectToMySQL('Books_ERD').query_db(query,data)
        
        print(results)
        
        author = cls(results[0])
        
        for book_in_author_fav in results:
            
            book_data = {
                "id" : book_in_author_fav['favorites.id'],
                "created_at" : book_in_author_fav['favorites.created_at'],
                "updated_at" : book_in_author_fav['favorites.updated_at'],
                "id" : book_in_author_fav['books.id'],
                "created_at" : book_in_author_fav['books.created_at'],
                "updated_at" : book_in_author_fav['books.updated_at']
            }
        
            author.favorites.append(books.Book(book_data))
        
        return author
            
        
    
