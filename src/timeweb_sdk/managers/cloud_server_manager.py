from timeweb_sdk.utils.base_client import BaseClient
from timeweb_sdk.entities import CloudServer, OS, ServerPreset, ServerConfig, Software


class CloudServerManager:
    """
    Cloud Server Manager

    Args:
        client (BaseClient):BaseClient, that executes requests to TimewebCloud API
    """

    def __init__(self, client: BaseClient):
        self.__client = client

    def get_all_servers(self) -> list[CloudServer]:
        response = self.__client.get("/servers")
        list_of_servers = []
        for server in response["servers"]:
            list_of_servers.append(CloudServer(self.__client, **server))
        return list_of_servers

    def get_server_by_id(self, server_id: int) -> CloudServer:
        response = self.__client.get(f"/servers/{server_id}")
        return CloudServer(self.__client, **response["server"])

    def get_os(self):
        response = self.__client.get("/os/servers")
        list_of_os = []
        for os in response["servers_os"]:
            list_of_os.append(OS(**os))
        return list_of_os

    def get_server_presets(self):
        response = self.__client.get("/presets/servers")
        list_of_server_presets = []
        for preset in response["server_presets"]:
            list_of_server_presets.append(ServerPreset(**preset))
        return list_of_server_presets

    def get_server_configs(self):
        response = self.__client.get("/configurator/servers")
        list_of_configs = []
        for config in response["server_configurators"]:
            list_of_configs.append(ServerConfig(**config))
        return list_of_configs

    def get_available_software(self):
        response = self.__client.get("/software/servers")
        list_of_software = []
        for software in response["servers_software"]:
            list_of_software.append(Software(**software))
        return list_of_software
