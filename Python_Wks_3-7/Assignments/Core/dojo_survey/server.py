from flask import Flask, render_template, request, redirect, session # added request and redirect

app = Flask(__name__)

app.secret_key = "safasl'ksdjf;oilsdajf;sdloifjj-09"

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/process', methods=["POST"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["fav_lang"] = request.form["fav_lang"]
    session["comment"] = request.form["comment"]
    # print(f"This is #2 request.form: {request.form}")
    return redirect("/result")

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)