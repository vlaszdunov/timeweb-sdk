from timeweb_sdk.managers._base import _Base
from typing import Literal
from warnings import deprecated


class CloudServerManager(_Base):
    __root_url = "https://api.timeweb.cloud/api/v1"
    __base_endpoint = f"{__root_url}/servers"

    def __init__(self, access_token):
        super().__init__(access_token)
        self.__access_token = access_token

    def get_list_of_servers(self):
        return self._make_request(
            "get",
            self.__base_endpoint,
        )

    def get_server_by_id(self, server_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}",
        )

    @deprecated("Deprecated! Use methods like ``shutdown_server()`` instead.")
    def execute_server_action(
        self,
        server_id: int,
        action: Literal[
            "hard_reboot",
            "hard_shutdown",
            "install",
            "reboot",
            "remove",
            "reset_password",
            "shutdown",
            "start",
            "clone",
        ],
    ):
        data = {"action": action}
        return self._make_request("post", f"{self.__base_endpoint}/{server_id}/action", data)

    def clone_server(self, server_id: int):
        return self._make_request("post", f"{self.__base_endpoint}/{server_id}/clone")

    def hard_shutdown_server(self, server_id: int):
        return self._make_request("post", f"{self.__base_endpoint}/{server_id}/hard-shutdown")

    def shutdown_server(self, server_id: int):
        return self._make_request("post", f"{self.__base_endpoint}/{server_id}/shutdown")

    def reset_server_password(self, server_id: int):
        return self._make_request("post", f"{self.__base_endpoint}/{server_id}/reset-password")

    def start_server(self, server_id: int):
        return self._make_request("post", f"{self.__base_endpoint}/{server_id}/start")

    def reboot_server(self, server_id: int):
        return self._make_request("post", f"{self.__base_endpoint}/{server_id}/reboot")

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

    def get_server_ips(self, server_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/ips",
        )

    def get_server_logs(self, server_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/logs",
        )

    def get_server_drives(self, server_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/disks",
        )

    def get_server_drive_by_id(self, server_id: int, drive_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}",
        )

    def get_drive_backup_settings(self, server_id: int, drive_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}/auto-backups",
        )

    def get_all_drive_backups(self, server_id: int, drive_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}/backups",
        )

    def get_drive_backup_by_id(self, server_id: int, drive_id: int, backup_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}/backups/{backup_id}",
        )
