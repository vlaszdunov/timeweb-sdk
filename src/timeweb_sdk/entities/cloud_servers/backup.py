from typing import Literal

__all__ = ["Backup"]

from timeweb_sdk.models import BackupModel
from timeweb_sdk.utils.base_client import BaseClient


class Backup:
    server_id: int
    drive_id: int
    id: int
    name: str
    comment: str
    created_at: str
    status: Literal[
        "precreate", "delete", "shutdown", "recover", "create", "fail", "done"
    ]
    size: int
    type: Literal["manual", "auto"]
    progress: int

    def __init__(self, client: BaseClient, server_id: int, drive_id: int, **kwargs):
        validated_data = BackupModel(**kwargs).model_dump()
        self.__client: BaseClient = client

        self.server_id = server_id
        self.drive_id = drive_id
        self.id = validated_data["id"]
        self.name = validated_data["name"]
        self.comment = validated_data["comment"]
        self.created_at = validated_data["created_at"]
        self.status = validated_data["status"]
        self.size = validated_data["size"]
        self.type = validated_data["type"]
        self.progress = validated_data["progress"]

    def rename_backup(self, comment: str):
        data = {"comment": comment}
        response = self.__client.patch(
            f"/servers/{self.server_id}/disks/{self.drive_id}/backups/{self.id}",
            data,
        )
        return Backup(**response["backup"])

    def restore(self):
        data = {"action": "restore"}
        self.__client.post(
            f"/servers/{self.server_id}/disks/{self.drive_id}/backups/{self.id}/action",
            data,
        )

    def mount(self):
        data = {"action": "mount"}
        self.__client.post(
            f"/servers/{self.server_id}/disks/{self.drive_id}/backups/{self.id}/action",
            data,
        )

    def unmount(self):
        data = {"action": "unmount"}
        self.__client.post(
            f"/servers/{self.server_id}/disks/{self.drive_id}/backups/{self.id}/action",
            data,
        )

    def delete(self):
        self.__client.delete(
            f"/servers/{self.server_id}/disks/{self.drive_id}/backups/{self.id}",
        )
