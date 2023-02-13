from flask import Flask, render_template, request, redirect, session # added request and redirect

app = Flask(__name__)

app.secret_key = "safasodhfosidhjoi2fwefj2o3rjf2ofi3j-09"

@app.route('/')
def index():
    session["counter"] = 1
    return render_template("index.html", title="", counter=session["counter"])

@app.route("/click")
def click():
    return redirect("/counter")

@app.route('/counter')
def counter():
    session["counter"] += 1
    return render_template("index.html", title="counter", counter=session["counter"])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
    