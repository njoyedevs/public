from flask import Flask, render_template, request, redirect, session # added request and redirect

app = Flask(__name__)
app.secret_key = "Keep it secret, keep it safe"
# our index route will handle rendering our form

@app.route('/play')
def index():
    return render_template("index.html", value=3)

@app.route('/play/<int:num>')
def input_number_boxes(num):
    return render_template("index.html", value=num)

@app.route('/play/<int:num>/<color>')
def input_num_color_boxes(num, color):
    return render_template("index.html", value=num, color=color)

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     # Here we add two properties to session to store the name and email
#     session['username'] = request.form['name']
#     session['useremail'] = request.form['email']
#     return redirect("/show")	

# # adding this method
# @app.route("/show")
# def show_user():
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return render_template("show.html", email=session['useremail'] )

if __name__ == "__main__":
    app.run(debug=True)