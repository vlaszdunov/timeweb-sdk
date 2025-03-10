from timeweb_sdk.managers._base import _Base
from typing import Optional


class CloudServerManager(_Base):
    __base_endpoint = "/servers"
    __get_servers = {"method": "get", "endpoint": __base_endpoint}

    def __init__(self, access_token):
        super().__init__(access_token)
        self.__base_endpoint = self._base_url + self.__base_endpoint
        self.__get_servers["endpoint"]: str = self.__base_endpoint

    def get_list_of_servers(self):
        return self.make_request(self.__get_servers["method"], self.__get_servers["endpoint"])
