from flask import request, jsonify
from flask_restful import Resource
import requests
import logging
from .auth import auth
from .config import USER_ROLES, OPA_URL
from .utils import log_request

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s',)
logger = logging.getLogger(__name__)

# Mock database
users_db = [
    {"name": "John Doe", "email": "john.doe@example.com"},
    {"name": "Jane Smith", "email": "jane.smith@example.com"}
]


class UserList(Resource):
    """
    Resource for handling user list retrieval.
    """

    @auth.login_required
    def get(self):
        """
        Handle GET requests to retrieve the list of users.

        Returns:
            response (json): The list of users or an error message.
        """
        token = auth.current_user()
        role = USER_ROLES[token]
        log_request(request)

        try:
            response = requests.post(OPA_URL, json={
                "input": {
                    "method": "GET",
                    "role": role
                }
            })
            response.raise_for_status()

            if response.json().get("result", False):
                return jsonify(users_db)
            else:
                logger.warning(f"Unauthorized access by role: {role}")
                return jsonify({"error": "Unauthorized"}), 403
        except requests.RequestException as e:
            logger.error(f"OPA request failed: {e}")
            return jsonify({"error": "Internal Server Error"}), 500


class User(Resource):
    """
    Resource for handling user creation.
    """

    @auth.login_required
    def post(self):
        """
        Handle POST requests to create a new user.

        Returns:
            response (json): The created user or an error message.
        """
        token = auth.current_user()
        role = USER_ROLES[token]
        log_request(request)

        try:
            response = requests.post(OPA_URL, json={
                "input": {
                    "method": "POST",
                    "role": role
                }
            })
            response.raise_for_status()

            if response.json().get("result", False):
                data = request.get_json()
                if not data or 'name' not in data or 'email' not in data:
                    return jsonify({"error": "Bad Request"}), 400

                users_db.append(data)
                return jsonify(data), 201
            else:
                logger.warning(f"Unauthorized access by role: {role}")
                return jsonify({"error": "Unauthorized"}), 403
        except requests.RequestException as e:
            logger.error(f"OPA request failed: {e}")
            return jsonify({"error": "Internal Server Error"}), 500
