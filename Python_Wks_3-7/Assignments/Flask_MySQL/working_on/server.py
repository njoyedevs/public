# Import app variable from __init__.py via flask_app folder
from flask_app import app

# Import the controller
from flask_app.controllers import friends_controller

if __name__ == "__main__":
    app.run(debug=True)

