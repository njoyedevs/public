from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",row=8,col=8,color1='red',color2='black')

@app.route('/<int:x>')
def row(x):
    return render_template("index.html",row=x,col=8,color1='red',color2='black')

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("index.html",row=x,col=y,color1='red',color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>')
def row_col_one(x,y,color1):
    return render_template("index.html",row=x,col=y,color1=color1,color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def row_col_two(x,y,color1,color2):
    return render_template("index.html",row=x,col=y,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)
    
# from flask import Flask, render_template, request, redirect, session # added request and redirect

# app = Flask(__name__)
# app.secret_key = "Keep it secret, keep it safe"
# # our index route will handle rendering our form

# @app.route('/')
# def index():
#     print(f"Works_1: 8x8")
#     height = 8
#     width = 8
#     return render_template("index.html", height=height, width=width)

# @app.route('/<int:num>')
# def input_x_boxes(num):
#     print(f"Works_2: 8x{num}")
#     height = 8
#     width= num
#     return render_template("index.html", height=height, width=width)

# @app.route('/<int:num_1>/<int:num_2>')
# def input_x_y_boxes(num_1, num_2):
#     print(f"Works_3: {num_1}x{num_2}")
#     height = num_1
#     width = num_2
#     return render_template("index.html", height=height, width=width)

# if __name__ == "__main__":
#     app.run(debug=True)