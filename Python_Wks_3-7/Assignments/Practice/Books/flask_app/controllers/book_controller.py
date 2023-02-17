from flask import render_template, redirect, request

from flask_app.models import books

from flask_app import app

@app.route('/books')
def books():
    return render_template('books.html', books=books.Book.get_all())

@app.route('/books/<int:id>')
def booksShow(id):
    data = {
        "id":id
    }
    return render_template('books_show.html', data=books.Book.get_books_fav_authors(data))

@app.route('/books/create', methods=["POST"])
def booksCreate():
    print(request.form)
    id = books.Book.save(request.form)
    
    return redirect(f"/books/<int:id>")