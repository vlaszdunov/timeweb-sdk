from timeweb_sdk.managers._base import _Base


class CloudServerManager(_Base):
    __root_url = "https://api.timeweb.cloud/api/v1"
    __base_endpoint = f"{__root_url}/servers"
    __get_servers = {"method": "get", "endpoint": __base_endpoint}
    __get_server = {"method": "get", "endpoint": f"{__base_endpoint}/server_id"}
    __get_os = {"method": "get", "endpoint": f"{__root_url}/os/servers"}
    __get_presets = {"method": "get", "endpoint": f"{__root_url}/presets/servers"}
    __get_configs = {"method": "get", "endpoint": f"{__root_url}/configurator/servers"}
    __get_software = {"method": "get", "endpoint": f"{__root_url}/software/server"}
    __get_server_ips = {"method": "get", "endpoint": f"{__base_endpoint}/server_id/ips"}
    __get_server_logs = {"method": "get", "endpoint": f"{__base_endpoint}/server_id/logs"}
    __get_server_drives = {"method": "get", "endpoint": f"{__base_endpoint}/server_id/disks"}
    __get_server_drive_by_id = {"method": "get", "endpoint": f"{__base_endpoint}/server_id/disks/drive_id"}
    __get_drive_autobackup_settings = {
        "method": "get",
        "endpoint": f"{__base_endpoint}/server_id/disks/drive_id/auto-backups",
    }
    __get_all_drive_backups = {"method": "get", "endpoint": f"{__base_endpoint}/server_id/disks/drive_id/backups"}
    __get_drive_backup_by_id = {
        "method": "get",
        "endpoint": f"{__base_endpoint}/server_id/disks/drive_id/backups/backup_id",
    }

    def __init__(self, access_token):
        super().__init__(access_token)

    def get_list_of_servers(self):
        return self.make_request(self.__get_servers["method"], self.__get_servers["endpoint"])

    def get_server_by_id(self, server_id: int):
        return self.make_request(
            self.__get_server["method"], self.__get_servers["endpoint"].replace("server_id", str(server_id))
        )

    def get_os(self):
        return self.make_request(self.__get_os["method"], self.__get_os["endpoint"])

    def get_server_presets(self):
        return self.make_request(self.__get_presets["method"], self.__get_presets["endpoint"])

    def get_server_configs(self):
        return self.make_request(self.__get_configs["method"], self.__get_configs["endpoint"])

    def get_available_software(self):
        return self.make_request(self.__get_software["method"], self.__get_software["endpoint"])

    def get_server_ips(self, server_id: int):
        return self.make_request(
            self.__get_server_ips["method"],
            self.__get_server_ips["endpoint"].replace("server_id", str(server_id)),
        )

    def get_server_logs(self, server_id: int):
        return self.make_request(
            self.__get_server_logs["method"],
            self.__get_server_logs["endpoint"].replace("server_id", str(server_id)),
        )

    def get_server_drives(self, server_id: int):
        return self.make_request(
            self.__get_server_drives["method"],
            self.__get_server_drives["endpoint"].replace("server_id", str(server_id)),
        )

    def get_server_drive_by_id(self, server_id: int, drive_id: int):
        return self.make_request(
            self.__get_server_drive_by_id["method"],
            self.__get_server_drive_by_id["endpoint"]
            .replace("server_id", str(server_id))
            .replace("drive_id", str(drive_id)),
        )

    def get_drive_backup_settings(self, server_id: int, drive_id: int):
        return self.make_request(
            self.__get_drive_autobackup_settings["method"],
            self.__get_drive_autobackup_settings["endpoint"]
            .replace("server_id", str(server_id))
            .replace("drive_id", str(drive_id)),
        )

    def get_all_drive_backups(self, server_id: int, drive_id: int):
        return self.make_request(
            self.__get_all_drive_backups["method"],
            self.__get_all_drive_backups["endpoint"]
            .replace("server_id", str(server_id))
            .replace("drive_id", str(drive_id)),
        )

    def get_drive_backup_by_id(self, server_id: int, drive_id: int, backup_id: int):
        return self.make_request(
            self.__get_drive_backup_by_id["method"],
            self.__get_drive_backup_by_id["endpoint"]
            .replace("server_id", str(server_id))
            .replace("drive_id", str(drive_id))
            .replace("backup_id", str(backup_id)),
        )
