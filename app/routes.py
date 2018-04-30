from app import app

@app.route('/')
@app.route('/index')
def index():
    """
    decorator creates an association between the URL given as an argument and
    the function
    :return: Greetings
    """
    return "Hello, World!"