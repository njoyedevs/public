from flask import Flask, render_template, request, redirect, session # added request and redirect

app = Flask(__name__)

app.secret_key = "safasl'ksdjf;oilsdajf;sdloifjj-09"

@app.route('/')
def index():
    session["name"] = ""
    session["location"] = "San Jose"
    session["favorite_lang"] = "Python"
    session["Comment"] = ""
    return render_template("index.html", name=session["name"], location=session["location"], fav_lang=session["favorite_lang"], comment=session["Comment"])

@app.route("/click", methods=["POST"])
def click():
    return redirect("/process")

@app.route('/process')
def process():
    
    return redirect("/result")

@app.route('/result')
def result():
    
    return render_template("result.html", name=session["name"], location=session["location"], fav_lang=session["favorite_lang"], comment=session["Comment"])
