from flask import Flask, render_template, request, redirect, session # added request and redirect

app = Flask(__name__)

app.secret_key = "safasl'ksdjf;oilsdajf;sdloifjj-09"

@app.route('/')
def index():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["fav_lang"] = request.form["fav_lang"]
    session["comments"] = request.form["comments"]
    session["key"] = "result"
    print(request.form)
    return render_template("index.html", name=session["name"], location=session["location"], fav_lang=session["fav_lang"], comment=session["comments"]) 

@app.route("/click", methods=["POST"])
def click():
    return redirect("/process")

@app.route('/process')
def process():
    addy = ""
    if session["key"] == "result":
        addy = "result"
    elif session["key"] == "index":
        addy = "index"
    print(request.form)
    return redirect(f"/{addy}")

@app.route('/result')
def result():
    session["key"] = "index"
    return render_template("result.html", name=session["name"], location=session["location"], fav_lang=session["favorite_lang"], comment=session["Comment"])

if __name__=="__main__":
    app.run(debug=True)