from flask import Flask

app = Flask(__name__)


from app import routes

routes.app #calling all route of routes.py



