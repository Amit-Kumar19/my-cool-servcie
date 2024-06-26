import os

# Mock user roles
USER_ROLES = {
    "admin-token": "admin",
    "user-token": "user"
}

# OPA URL
OPA_URL = os.getenv('OPA_URL', 'http://opa-service:8181/v1/data/authz/allow')

