from flask import render_template, redirect, request

from flask_app.models import authors

from flask_app import app

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def dojo():
    return render_template('authors.html', authors=authors.Author.get_all())

@app.route('/authors/<int:id>')
def authorsShow(id):
    data = {
        "id":id
    }
    return render_template('authors_show.html', data=authors.Author.get_authors_fav_books(data))


@app.route('/authors/create', methods=["POST"])
def authorsCreate():
    authors.Author.save(request.form)
    return redirect('/authors')

