import json
from collections import OrderedDict
from http.client import HTTPException
from typing import Optional, Literal
from timeweb_sdk.utils.exceptions import *
from timeweb_sdk.utils import BearerAuth
from httpx import get, post, delete, patch, codes, Response


class _Base:
    def __init__(self, access_token):
        self.__access_token = access_token

    def _make_request(
        self,
        method: Literal["get", "post", "patch", "delete"],
        endpoint: str,
        data: dict = Optional[None],
    ) -> dict | HTTPException | None:
        match method:
            case "get":
                response: Response = self.__get(endpoint)
            case "post":
                response: Response = self.__post(endpoint, data)
            case "patch":
                response: Response = self.__patch(endpoint, data)
            case "delete":
                response: Response = self.__delete(endpoint)
            case _:
                raise ValueError("Invalid request method")

        match response.status_code:
            case codes.OK | codes.CREATED:
                return json.loads(response.text, object_hook=lambda pairs: OrderedDict(pairs))
            case codes.NO_CONTENT:
                pass
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

    def __get(self, endpoint) -> Response:
        response = get(
            url=endpoint,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )
        return response

    def __post(self, endpoint, data) -> Response:
        response = post(
            url=endpoint,
            json=data,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )
        return response

    def __patch(self, endpoint, data) -> Response:
        response = patch(
            url=endpoint,
            json=data,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )
        return response

    def __delete(self, endpoint) -> Response:
        response = delete(
            url=endpoint,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )
        return response
