from typing import Optional, Literal

from timeweb_sdk.utils import BearerAuth
from httpx import get, post, delete, put, patch


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
                return self.__delete(endpoint, data)

    def __get(self, endpoint):
        return get(
            url=endpoint,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )

    def __post(self, endpoint, data):
        return post(
            url=endpoint,
            json=data,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )

    def __patch(self, endpoint, data):
        return patch(
            url=endpoint,
            json=data,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )

    def __delete(self, endpoint, data):
        return delete(
            url=endpoint,
            auth=BearerAuth(self.__access_token),
            headers={"Content-Type": "application/json"},
        )
