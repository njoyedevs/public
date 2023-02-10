from flask import Flask, render_template, request, redirect, session # added request and redirect

app = Flask(__name__)
app.secret_key = "Keep it secret, keep it safe"
# our index route will handle rendering our form

# app name
@app.errorhandler(404)

# Function that takes error as parameter
def not_found(e):
    
    # returns 404 message
    return "Sorry! No response. Try again."

@app.route('/')
def index():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<person_name>')
def hi_person(person_name):
    return 'Hi ' + f"{person_name}"

@app.route('/repeat/<int:num>/<string:word>')
def statements(num, word):
    return f"{word}"*num

# @app.route('/dojo')
# def dojo():
#     render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)