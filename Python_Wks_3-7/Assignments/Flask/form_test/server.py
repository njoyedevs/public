from flask import Flask, render_template, request, redirect, session # added request and redirect

app = Flask(__name__)
app.secret_key = "Keep it secret, keep it safe"
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     print(request.form['name'])
#     # Never render a template on a POST request.
#     # # Instead we will redirect to our index route.
    
#     # When we have finished processing the POST data,
#     # we can perform a GET request on behalf of the client,
#     # which will now be the request that is completed should the
#     # client refresh the page. This is called
#     # redirecting. Always redirect after handling
#     # POST data to avoid data being handled more
#     # than once!#
    
#     return redirect('/')    
    
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")	 

# adding this method
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html", email=session['useremail'] )

if __name__ == "__main__":
    app.run(debug=True)

