from flask import Flask 
from flask_restful import Api

from .extensions import db
from .resource.user import UserResource, UsersResource

def create_app():
    app = Flask(__name__)

    app.config['MONGODB_SETTINGS'] = {
        'db': 'python',
        'host': 'localhost',
        'port': 27017
    }

    db.init_app(app)
    api = Api(app)
    api.add_resource(UsersResource, '/users')
    api.add_resource(UserResource, '/user/<name>')
    return app