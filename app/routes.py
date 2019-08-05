
from app import app #__init__.py
from flask import render_template


@app.route('/')
def hello_world():
    return "<h1>Hello , World!</h1>"


@app.route('/index')
def index():
    return render_template('index.htm' , login=False)


@app.route('/courses')
def courses():
    return render_template('courses.htm' , login=False)


@app.route('/register')
def register():
    return render_template('register.htm' , login=False)


@app.route('/login')
def login():
    return render_template('login.htm' , login=False)


