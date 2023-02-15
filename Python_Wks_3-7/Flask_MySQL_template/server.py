# Import app variable from the __init__.py via flask_app folder
from flask_app import app

# Import the controllers via flask_app.controllers folders
from flask_app.controllers import users_controller

# Create if statement that will verify the script running is the "__main__" script
if __name__ == "__main__":
    
    # use the imported app variable holding the Flask instance to call run function 
    # with debugging turned on.
    app.run(debug=True)