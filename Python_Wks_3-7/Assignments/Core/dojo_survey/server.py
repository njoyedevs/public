from flask import Flask, render_template, request, redirect, session # added request and redirect

app = Flask(__name__)

app.secret_key = "safasl'ksdjf;oilsdajf;sdloifjj-09"

@app.route('/')
def index():
    session["key"] = "result"
    # session["name"] = request.form["name"]
    # session["location"] = request.form["location"]
    # session["fav_lang"] = request.form["fav_lang"]
    # session["comment"] = request.form["comment"]
    session["name"] = "Nicolas"
    session["location"] = "San Jose"
    session["fav_lang"] = "Python"
    session["comment"] = "Testing Comments"
    print(f"This is #2 request.form: {request.form}")
    return render_template("index.html", name=session["name"], location=session["location"], fav_lang=session["fav_lang"], comment=session["comment"]) 
    # return render_template("index.html")

@app.route("/click", methods=["POST"])
def click():
    return redirect("/process")

@app.route('/process')
def process():
    addy = ""
    if session["key"] == "result":
        addy = "result"
    elif session["key"] == "index":
        addy = ""
    print(f"This is #2 request.form: {request.form}")
    return redirect(f"/{addy}")

@app.route('/result')
def result():
    session["key"] = "index"
    return render_template("result.html", name=session["name"], location=session["location"], fav_lang=session["fav_lang"], comment=session["comment"])

if __name__=="__main__":
    app.run(debug=True)