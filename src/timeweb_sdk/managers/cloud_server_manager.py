from timeweb_sdk.managers._base import _Base
from typing import Literal, Annotated, Optional
from annotated_types import Ge, Le
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

    def change_boot_mode(self, server_id: int, boot_mode: Literal["default", "single", "reset-password"]):
        data = {"boot_mode": boot_mode}
        return self._make_request("post", f"{self.__base_endpoint}/{server_id}/boot-mode", data)

    def set_nat_mode(self, server_id: int, nat_mode: Literal["dnat_and_snat", "dnat_and_snat", "snat"]):
        data = {"nat_mode": nat_mode}
        return self._make_request(
            "patch",
            f"{self.__base_endpoint}/{server_id}/local-networks/nat-mode",
            data,
        )

    def get_server_ips(self, server_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/ips",
        )

    def add_server_ip(self, server_id: int, ip_type: Literal["ipv4", "ipv6"], ptr: Optional[str] = None):
        data = {"type": ip_type, "ptr": ptr}
        return self._make_request(
            "patch",
            f"{self.__base_endpoint}/{server_id}/ips",
            data,
        )

    def delete_server_ip(self, server_id: int, server_ip: str):
        data = {"ip": server_ip}
        return self._make_request(
            "delete",
            f"{self.__base_endpoint}/{server_id}/ips",
            data,
        )

    def change_server_ip(self, server_id: int, server_ip: str, ptr: str):
        data = {"ip": server_ip, "ptr": ptr}
        return self._make_request(
            "delete",
            f"{self.__base_endpoint}/{server_id}/ips",
            data,
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

    def create_server_drive(
        self,
        server_id: int,
        drive_size: Annotated[int, Ge(5120), Le(512000)],
    ):
        data = {"size": drive_size}
        return self._make_request(
            "post",
            f"{self.__base_endpoint}/{server_id}/disks",
            data,
        )

    def get_server_drive_by_id(self, server_id: int, drive_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}",
        )

    def change_server_drive_settings(self, server_id: int, drive_id: int, drive_size: Annotated[int, Ge(ge=5120)]):
        data = {"size": drive_size}
        return self._make_request(
            "patch",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}",
            data,
        )

    def delete_server_drive(self, server_id: int, drive_id: int):
        return self._make_request("delete", f"{self.__base_endpoint}/{server_id}/disks/{drive_id}")

    def get_drive_backup_settings(self, server_id: int, drive_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}/auto-backups",
        )

    def create_drive_backup(self, server_id: int, drive_id: int, comment: Optional[str]):
        data = {"comment": comment}
        return self._make_request(
            "post",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}/backups",
            data,
        )

    def get_all_drive_backups(self, server_id: int, drive_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}/backups",
        )

    def change_drive_backup(self, server_id: int, drive_id: int, backup_id: int, comment: str):
        data = {"comment": comment}
        return self._make_request(
            "patch",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}/backups/{backup_id}",
            data,
        )

    def delete_drive_backup(self, server_id: int, drive_id: int, backup_id: int):
        return self._make_request(
            "delete",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}/backups/{backup_id}",
        )

    def get_drive_backup_by_id(self, server_id: int, drive_id: int, backup_id: int):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}/backups/{backup_id}",
        )

    def execute_backup_action(
        self,
        server_id: int,
        drive_id: int,
        backup_id: int,
        action: Literal["restore", "mount", "unmount"],
    ):
        data = {"action": action}
        return self._make_request(
            "post",
            f"{self.__base_endpoint}/{server_id}/disks/{drive_id}/backups/{backup_id}/action",
            data,
        )

    def unmount_iso_and_reboot(self, server_id: int):
        return self._make_request(
            "post",
            f"{self.__base_endpoint}/{server_id}/image-unmount",
            data={},
        )
