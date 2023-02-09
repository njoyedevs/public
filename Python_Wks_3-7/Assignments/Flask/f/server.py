from flask import Flask, render_template, request, redirect # added request and redirect

app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")

from flask import Flask, render_template, request, redirect # added request and redirect
            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    print(request.form['name'])
    # Never render a template on a POST request.
    # # Instead we will redirect to our index route.
    
    # When we have finished processing the POST data,
    # we can perform a GET request on behalf of the client,
    # which will now be the request that is completed should the
    # client refresh the page. This is called
    # redirecting. Always redirect after handling
    # POST data to avoid data being handled more
    # than once!#
    
    return redirect('/')    

if __name__ == "__main__":
    app.run(debug=True)

