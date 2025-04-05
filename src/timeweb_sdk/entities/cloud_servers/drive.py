from typing import Annotated, Optional

from annotated_types import Ge, Le

from timeweb_sdk.utils._base import _Base
from timeweb_sdk.models import DriveModel
from .backup import Backup

__all__ = ["Drive"]


class Drive(_Base):
    __root_url = "https://api.timeweb.cloud/api/v1"
    __base_endpoint = f"{__root_url}/servers"
    __api_token: str

    id: int
    server_id: int
    size: int
    used: int
    type: str
    is_mounted: bool
    is_system: bool
    system_name: str
    status: str

    def __init__(self, api_token: str, server_id: int, **kwargs):
        validated_data = DriveModel(**kwargs).model_dump()
        super().__init__(api_token)

        self.__api_token = api_token
        self.id = validated_data["id"]
        self.server_id = server_id
        self.size = validated_data["size"]
        self.used = validated_data["used"]
        self.type = validated_data["type"]
        self.is_mounted = validated_data["is_mounted"]
        self.is_system = validated_data["is_system"]
        self.system_name = validated_data["system_name"]
        self.status = validated_data["status"]

    def change_size(self, drive_size: Annotated[int, Ge(5120), Le(512000)]):
        data = {"size": drive_size}
        response = self._make_request(
            "patch",
            f"{self.__base_endpoint}/{self.server_id}/disks/{self.id}",
            data,
        )
        return Drive(self.__api_token, self.server_id, **response["server_disk"])

    def delete(self):
        self._make_request(
            "delete",
            f"{self.__base_endpoint}/{self.server_id}/disks/{self.id}",
        )

    def get_all_backups(self):
        response = self._make_request(
            "get",
            f"{self.__base_endpoint}/{self.server_id}/disks/{self.id}/backups",
        )
        backups = [Backup(self.__api_token, self.server_id, self.id, **backup) for backup in response["backups"]]
        return backups

    def create_backup(self, drive_id: int, comment: Optional[str]):
        data = {"comment": comment}
        response = self._make_request(
            "post",
            f"{self.__base_endpoint}/{self.server_id}/disks/{self.id}/backups",
            data,
        )
        return Backup(self.__api_token, self.server_id, **response["backup"])

    def get_autobackup_settings(self):
        return self._make_request(
            "get",
            f"{self.__base_endpoint}/{self.server_id}/disks/{self.id}/auto-backups",
        )
