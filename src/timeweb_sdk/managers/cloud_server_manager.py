from timeweb_sdk.utils._base import _Base
from timeweb_sdk.entities import CloudServer, OS, ServerPreset


class CloudServerManager(_Base):
    __root_url = "https://api.timeweb.cloud/api/v1"
    __base_endpoint = f"{__root_url}/servers"

    def __init__(self, api_token):
        super().__init__(api_token)
        self.__api_token = api_token

    def get_all_servers(self) -> list[CloudServer]:
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
        response = self._make_request(
            "get",
            f"{self.__root_url}/os/servers",
        )
        list_of_os = []
        for os in response["servers_os"]:
            list_of_os.append(OS(**os))
        return list_of_os

    def get_server_presets(self):
        response = self._make_request(
            "get",
            f"{self.__root_url}/presets/servers",
        )
        list_of_server_presets = []
        for preset in response["server_presets"]:
            list_of_server_presets.append(ServerPreset(**preset))
        return list_of_server_presets

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
