from timeweb_sdk.managers._base import _Base
from typing import Optional


class CloudServerManager(_Base):
    __root_url = "https://api.timeweb.cloud/api/v1"
    __base_endpoint = f"{__root_url}/servers"
    __get_servers = {"method": "get", "endpoint": __base_endpoint}
    __get_server = {"method": "get", "endpoint": __base_endpoint}
    __get_os = {"method": "get", "endpoint": f"{__root_url}/os/servers"}

    def __init__(self, access_token):
        super().__init__(access_token)

    def get_list_of_servers(self):
        return self.make_request(self.__get_servers["method"], self.__get_servers["endpoint"])

    def get_server_by_id(self, server_id: int):
        return self.make_request(self.__get_server["method"], self.__get_servers["endpoint"] + f"/{server_id}")

    def get_os(self):
        return self.make_request(self.__get_os["method"], self.__get_os["endpoint"])
