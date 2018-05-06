# Python script at the top-level that defines the Flask application instance

from app import app

# Flask needs to be told how to import it, by setting the FLASK_APP
# environment variable:
# export FLASK_APP=cryptocurrencies.py

if __name__ == '__main__':
    """
    Single page flask app example
    """
    from flask import Flask
    myapp = Flask(__name__)

    @myapp.route('/')
    def hello_world():
        return 'Single page flask app!'

    myapp.run(host='0.0.0.0')
