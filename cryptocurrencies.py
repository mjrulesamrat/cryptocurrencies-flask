# Python script at the top-level that defines the Flask application instance

from app import app

# Flask needs to be told how to import it, by setting the FLASK_APP
# environment variable:
# export FLASK_APP=cryptocurrencies.py