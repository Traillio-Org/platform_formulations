import requests as req

def handle_request_error(err):
    """Handles different types of request exceptions."""
    if isinstance(err, req.exceptions.HTTPError):
        print(f"HTTP error occurred: {err}")
    elif isinstance(err, req.exceptions.ConnectionError):
        print("Error: Unable to connect to the API.")
    elif isinstance(err, req.exceptions.Timeout):
        print("Error: The request timed out.")
    elif isinstance(err, req.exceptions.RequestException):
        print(f"Request error: {err}")