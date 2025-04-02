from typing import Literal

__all__ = ["Backup"]

from timeweb_sdk.models import BackupModel
from timeweb_sdk.utils._base import _Base


class Backup(_Base):
    __root_url = "https://api.timeweb.cloud/api/v1"
    __base_endpoint = f"{__root_url}/servers"
    __api_token: str

    server_id: int
    drive_id: int
    id: int
    name: str
    comment: str
    created_at: str
    status: Literal["precreate", "delete", "shutdown", "recover", "create", "fail", "done"]
    size: int
    type: Literal["manual", "auto"]
    progress: int

    def __init__(self, api_token: str, server_id: int, drive_id: int, **kwargs):
        validated_data = BackupModel(**kwargs).model_dump()
        super().__init__(api_token)

        self.__api_token = api_token
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
        response = self._make_request(
            "patch",
            f"{self.__base_endpoint}/{self.server_id}/disks/{self.drive_id}/backups/{self.id}",
            data,
        )
        return Backup(**response["backup"])

    def restore(self):
        data = {"action": "restore"}
        self._make_request(
            "post",
            f"{self.__base_endpoint}/{self.server_id}/disks/{self.drive_id}/backups/{self.id}/action",
            data,
        )

    def mount(self):
        data = {"action": "mount"}
        self._make_request(
            "post",
            f"{self.__base_endpoint}/{self.server_id}/disks/{self.drive_id}/backups/{self.id}/action",
            data,
        )

    def unmount(self):
        data = {"action": "unmount"}
        self._make_request(
            "post",
            f"{self.__base_endpoint}/{self.server_id}/disks/{self.drive_id}/backups/{self.id}/action",
            data,
        )

    def delete(self):
        self._make_request(
            "delete",
            f"{self.__base_endpoint}/{self.server_id}/disks/{self.drive_id}/backups/{self.id}",
        )
