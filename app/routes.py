from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    """
    decorator creates an association between the URL given as an argument and
    the function
    :return: Greetings
    """
    data = {
        'title': "Hello Y'all",
        'greeting': 'Welcome to Flask meetup :)'
    }
    return render_template('index.html', data=data)
