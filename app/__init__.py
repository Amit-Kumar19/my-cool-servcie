from flask import Flask
from flask_restful import Api
from .main import UserList, User
from .auth import auth


def create_app():
    """
    Create and configure the Flask application.

    Returns:
        app (Flask): The configured Flask application instance.
    """
    app = Flask(__name__)
    api = Api(app)

    # Register resources
    api.add_resource(UserList, '/api/users')
    api.add_resource(User, '/api/users')

    return app
