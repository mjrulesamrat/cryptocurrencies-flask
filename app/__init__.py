from flask import Flask

# creates the application object as an instance of class Flask
# imported from the flask package
app = Flask(__name__)

from app import routes