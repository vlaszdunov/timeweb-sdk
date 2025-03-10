from typing import Optional

from timeweb_sdk.utils import BearerAuth
from httpx import get, post


class _Base:
    def __init__(self, access_token):
        self.__access_token = access_token

    __root_url: str = "https://api.timeweb.cloud/api"
    __api_version: str = "/v1"
    _base_url: str = __root_url + __api_version

    def make_request(self, method: str, endpoint, data: dict = Optional[None]):
        match method:
            case "get":
                return self._get(endpoint)
            case "post":
                return self._post(endpoint, data)

    def _get(self, endpoint):
        return get(url=endpoint, auth=BearerAuth(self.__access_token), headers={"Content-Type": "application/json"})

    def _post(self, endpoint, data):
        return post(
            url=endpoint, json=data, auth=BearerAuth(self.__access_token), headers={"Content-Type": "application/json"}
        )
