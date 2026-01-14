import json
from collections import OrderedDict
from typing import Any
from timeweb_sdk.utils.exceptions import *
from timeweb_sdk.utils import BearerAuth
from httpx import Client, Response, codes
import jwt

__all__ = ["BaseClient"]


class BaseClient:
    """
    Args:
        access_token (str): Timeweb Cloud Bearer API token
    """

    def __init__(self, access_token: str) -> None:
        self.__verify_token(access_token)
        self.__client = Client(
            auth=BearerAuth(access_token),
            base_url="https://api.timeweb.cloud/api/v1",
            headers={"Content-Type": "application/json"},
            http2=True,
        )

    def close_client(self) -> None:
        self.__client.close()

    def __verify_token(self, access_token: str) -> None:
        """
        Validates the access token

        Args:
            access_token (str): Timeweb Cloud Bearer API token

        Raises:
            ExpiredAccessTokenError: If the access token is expired
            InvalidToken: If the access token is invalid
        """
        try:
            jwt.decode(
                access_token,
                options={
                    "verify_signature": False,
                    "verify_exp": True,
                    "verify_nbf": True,
                },
            )
        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredAccessTokenError() from None
        except jwt.exceptions.InvalidTokenError or jwt.exceptions.ImmatureSignatureError:
            raise InvalidToken() from None

    def get(self, url: str, params: dict | None = None) -> dict:
        response = self.__client.get(url=url, params=params)
        self.__validate_http_response(response)
        return response.json()

    def post(self, url: str, data: dict | None = None) -> dict:
        response = self.__client.post(url=url, json=data)
        self.__validate_http_response(response)
        return response.json()

    def delete(self, url: str, params: dict | None = None, data: dict | None = None) -> dict:
        # response = self.__client.delete(url=url, params=params)
        request = self.__client.build_request("DELETE", url=url, json=data, params=params)
        response = self.__client.send(request)
        self.__validate_http_response(response)
        return response.json()

    def patch(self, url: str, params: dict | None = None, data: dict | None = None) -> dict:
        response = self.__client.patch(url=url, data=data)
        self.__validate_http_response(response)
        return response.json()

    def __validate_http_response(self, response: Response) -> Any | None:
        match response.status_code:
            case codes.OK | codes.CREATED:
                return json.loads(response.text, object_hook=lambda pairs: OrderedDict(pairs))
            case codes.NO_CONTENT:
                return None
            case codes.BAD_REQUEST:
                raise HTTPBadRequestError(response.json()["message"])
            case codes.UNAUTHORIZED:
                raise HTTPUnauthorizedError(response.json()["message"])
            case codes.FORBIDDEN:
                raise HTTPForbiddenError(response.json()["message"])
            case codes.NOT_FOUND:
                raise HTTPNotFoundError(response.json()["message"])
            case codes.TOO_MANY_REQUESTS:
                raise HTTPTooManyRequestsError(response.json()["message"])
            case codes.INTERNAL_SERVER_ERROR:
                raise HTTPInternalServerError(response.json()["message"])
            case codes.LOCKED:
                raise HTTPLockedError(response.json()["message"])
        return None
