import logging

logger = logging.getLogger(__name__)


def log_request(request):
    """
    Log the details of the incoming request.

    Args:
        request (Request): The Flask request object.
    """
    logger.info(f"Request: {request.method} {request.path}")
    logger.info(f"Headers: {dict(request.headers)}")
    logger.info(f"Body: {request.get_data(as_text=True)}")
