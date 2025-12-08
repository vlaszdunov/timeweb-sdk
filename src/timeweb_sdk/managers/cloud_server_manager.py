import warnings

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

    def create_server(
        self,
        server_name: str,
        bandwidth: int,
        configuration: ServerConfig | None = None,
        preset_id: int | None = None,
        os_id: int | None = None,
        image_id: int | None = None,
        comment: str | None = None,
        avatar_id: str | None = None,
        software_id: int | None = None,
        ssh_keys_id: int | None = None,
        is_local_network: bool | None = None,
        is_ddos_guard: bool | None = False,
        network: dict | None = None,
        availability_zone: str | None = None,
        is_root_password_required: bool | None = None,
        project_id: int | None = None,
    ):
        if avatar_id is not None:
            warnings.warn("Deprecated!", DeprecationWarning)
        if is_local_network is not None:
            warnings.warn("Deprecated!", DeprecationWarning)

        if configuration and preset_id is None:
            raise ValueError(
                "One of these parameters is required: preset_id, configuration"
            )
        if image_id and os_id is None:
            raise ValueError("One of these parameters is required: image_id, os_id")
        data = {
            "name": server_name,
            "bandwidth": bandwidth,
            **({"configuration": configuration} if configuration is not None else {}),
            **({"preset_id": preset_id} if preset_id is not None else {}),
            **({"os_id": os_id} if os_id is not None else {}),
            **({"image_id": image_id} if image_id is not None else {}),
            **({"comment": comment} if comment is not None else {}),
            **({"avatar_id": avatar_id} if avatar_id is not None else {}),
            **({"software_id": software_id} if software_id is not None else {}),
            **({"ssh_keys_id": ssh_keys_id} if ssh_keys_id is not None else {}),
            **(
                {"is_local_network": is_local_network}
                if is_local_network is not None
                else {}
            ),
            **({"is_ddos_guard": is_ddos_guard} if is_ddos_guard is not None else {}),
            **({"network": network} if network is not None else {}),
            **(
                {"availability_zone": availability_zone}
                if availability_zone is not None
                else {}
            ),
            **(
                {"is_root_password_required": is_root_password_required}
                if is_root_password_required is not None
                else {}
            ),
            **({"project_id": project_id} if project_id is not None else {}),
        }

        return self.__client.post("/servers", data=data)

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
