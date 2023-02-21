from flask import Flask
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
BCRYPT = Bcrypt(app) 

app.secret_key = "645-0sdfgersytgse534g5rthgrtsurtu9"

DATABASE = 'message_app'