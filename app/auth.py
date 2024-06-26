from flask_httpauth import HTTPTokenAuth
from .config import USER_ROLES

auth = HTTPTokenAuth(scheme='Bearer')


@auth.verify_token
def verify_token(token):
    """
    Verify the provided token and return the associated role.

    Args:
        token (str): The token to verify.

    Returns:
        str: The role associated with the token, or None if the token is invalid.
    """
    if token in USER_ROLES:
        return token
    return None
