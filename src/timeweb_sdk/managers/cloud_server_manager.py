from timeweb_sdk.utils._base import _Base
from timeweb_sdk.entities import CloudServer


class CloudServerManager(_Base):
    __root_url = "https://api.timeweb.cloud/api/v1"
    __base_endpoint = f"{__root_url}/servers"

    def __init__(self, api_token):
        super().__init__(api_token)
        self.__api_token = api_token

    def get_list_of_servers(self) -> list[CloudServer]:
        response = self._make_request(
            "get",
            self.__base_endpoint,
        )
        list_of_servers = []
        for server in response["servers"]:
            list_of_servers.append(CloudServer(self.__api_token, **server))
        return list_of_servers

    def get_server_by_id(self, server_id: int) -> CloudServer:
        response = self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}",
        )
        return CloudServer(self.__api_token, **response["server"])

    def get_os(self):
        return self._make_request(
            "get",
            f"{self.__root_url}/os/servers",
        )

    def get_server_presets(self):
        return self._make_request(
            "get",
            f"{self.__root_url}/presets/servers",
        )

    def get_server_configs(self):
        return self._make_request(
            "get",
            f"{self.__root_url}/configurator/servers",
        )

    def get_available_software(self):
        return self._make_request(
            "get",
            f"{self.__root_url}/software/servers",
        )
