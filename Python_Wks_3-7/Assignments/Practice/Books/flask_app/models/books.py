from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import authors

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['first_name']
        self.num_of_pages = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorites = []
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM books;'
        results = connectToMySQL('Books_ERD').query_db(query)
        
        books = []
        
        for result in results:
            books.append(result)
            
        return books
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL('Books_ERD').query_db(query, data)
        print(results)
        return cls(results[0])
    
    @classmethod
    def save(cls,data):
        query = """INSERT INTO books (title, num_of_pages, 
                created_at, updated_at, author_id) Values
                (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(author_id)s);"""
                
        return connectToMySQL('Books_ERD').query_db(query,data)
    
    @classmethod
    def get_books_fav_authors(cls,data):
        
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id=books.id LEFT JOIN authors ON favorites.author_id=authors.id WHERE books.id = %(id)s;"
        
        results = connectToMySQL('Books_ERD').query_db(query,data)
        
        print(results)
        
        book = cls(results[0])
        
        for author_in_book_fav in results:
            
            author_data = {
                "id" : author_in_book_fav['favorites.id'],
                "created_at" : author_in_book_fav['favorites.created_at'],
                "updated_at" : author_in_book_fav['favorites.updated_at'],
                "id" : author_in_book_fav['authors.id'],
                "created_at" : author_in_book_fav['authors.created_at'],
                "updated_at" : author_in_book_fav['authors.updated_at']
            }
        
            book.favorites.append(authors.Author(author_data))
        
        return book