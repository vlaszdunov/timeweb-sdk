import json
from collections import OrderedDict
from typing import Optional, Literal
from timeweb_sdk.utils.exceptions import *
from timeweb_sdk.utils import BearerAuth
from httpx import get, post, delete, patch, codes, Response


def _match_responses(response: Response):
    match response.status_code:
        case codes.OK | codes.CREATED:
            return json.loads(response.text, object_hook=lambda pairs: OrderedDict(pairs))
        case codes.NO_CONTENT:
            return
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


class _Base:
    def __init__(self, access_token):
        self.__access_token = access_token

    def _make_request(self, method: Literal["get", "post", "patch", "delete"], endpoint, data: dict = Optional[None]):
        match method:
            case "get":
                return self.__get(endpoint)
            case "post":
                return self.__post(endpoint, data)
            case "patch":
                return self.__patch(endpoint, data)
            case "delete":
                return self.__delete(endpoint)

    def __get(self, endpoint):
        response = get(
            url=endpoint,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )
        _match_responses(response)

    def __post(self, endpoint, data):
        response = post(
            url=endpoint,
            json=data,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )
        _match_responses(response)

    def __patch(self, endpoint, data):
        response = patch(
            url=endpoint,
            json=data,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )
        _match_responses(response)

    def __delete(self, endpoint):
        response = delete(
            url=endpoint,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )
        _match_responses(response)
