from flask import Flask
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
BCRYPT = Bcrypt(app) 

app.secret_key = "safasl25366534654634564ertdfgdfshgoifjj-09"

DATABASE = 'message_app'
