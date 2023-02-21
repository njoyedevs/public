from flask import Flask
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
BCRYPT = Bcrypt(app) 

app.secret_key = "645-smsjsdjsus8s84u4jh4j4j4j4nnrjfjfhydujkdekmdidurtu9"

DATABASE = 'recipes'