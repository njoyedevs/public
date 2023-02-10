from flask import Flask, render_template, request, redirect, session # added request and redirect

app = Flask(__name__)
app.secret_key = "Keep it secret, keep it safe"
# our index route will handle rendering our form

@app.route('/')
def index():
    print(f"Works_1: 8x8")
    height = 8
    width = 8
    return render_template("index.html", height=height, width=width)

@app.route('/<int:num>')
def input_x_boxes(num):
    print(f"Works_2: 8x{num}")
    height = 8
    width= num
    return render_template("index.html", height=height, width=width)

@app.route('/<int:num_1>/<int:num_2>')
def input_x_y_boxes(num_1, num_2):
    print(f"Works_3: {num_1}x{num_2}")
    height = num_1
    width = num_2
    return render_template("index.html", height=height, width=width)

if __name__ == "__main__":
    app.run(debug=True)