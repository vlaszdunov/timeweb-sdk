__all__ = [
    "HTTPBadRequestError",
    "HTTPUnauthorizedError",
    "HTTPForbiddenError",
    "HTTPNotFoundError",
    "HTTPTooManyRequestsError",
    "HTTPInternalServerError",
]


class HTTPError(HTTPError):
    """Base exception class for all HTTP-related errors."""


class HTTPBadRequestError(HTTPError):
    """HTTP 400 Bad Request"""

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class HTTPUnauthorizedError(HTTPError):
    """HTTP 401 Not Authorized"""

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class HTTPForbiddenError(HTTPError):
    """HTTP 403 Forbidden"""

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class HTTPNotFoundError(HTTPError):
    """HTTP 404 Not Found"""

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class HTTPTooManyRequestsError(HTTPError):
    """HTTP 429 Too Many Requests"""

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class HTTPInternalServerError(HTTPError):
    """HTTP 500 Internal Server Error"""

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message
