from typing import Annotated, Optional

from annotated_types import Ge, Le

from timeweb_sdk.utils.base_client import BaseClient
from timeweb_sdk.models import DriveModel
from .backup import Backup

__all__ = ["Drive"]


class Drive:
    id: int
    server_id: int
    size: int
    used: int
    type: str
    is_mounted: bool
    is_system: bool
    system_name: str
    status: str

    def __init__(self, client: BaseClient, server_id: int, **kwargs):
        validated_data = DriveModel(**kwargs).model_dump()
        self.__client = client

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
        response = self.__client.patch(
            f"/servers/{self.server_id}/disks/{self.id}",
            data,
        )
        return Drive(self.__client, self.server_id, **response["server_disk"])

    def delete(self):
        self.__client.delete(
            f"/servers/{self.server_id}/disks/{self.id}",
        )

    def get_all_backups(self):
        response = self.__client.get(
            f"/servers/{self.server_id}/disks/{self.id}/backups",
        )
        backups = [
            Backup(self.__api_token, self.server_id, self.id, **backup)
            for backup in response["backups"]
        ]
        return backups

    def create_backup(self, comment: Optional[str]):
        data = {"comment": comment}
        response = self.__client.post(
            f"/servers/{self.server_id}/disks/{self.id}/backups",
            data,
        )
        return Backup(self.__client, self.server_id, self.id, **response["backup"])

    def get_autobackup_settings(self):
        return self.__client.get(
            f"/servers/{self.server_id}/disks/{self.id}/auto-backups",
        )
