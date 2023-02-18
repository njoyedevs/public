from flask_app import app

from flask_app.controllers import logins_controller
from flask_app.controllers import messages_controller
from flask_app.controllers import comments_controller

if __name__ == "__main__":
    app.run(debug=True)