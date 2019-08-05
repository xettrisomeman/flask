
from app import app #__init__.py



@app.route('/')
def hello_world():
    return "<h1>Hello , World!</h1>"


