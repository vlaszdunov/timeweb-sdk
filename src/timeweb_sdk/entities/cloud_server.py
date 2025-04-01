from typing import Any, Literal
from warnings import deprecated
from timeweb_sdk.utils._base import _Base
from timeweb_sdk.models import CloudServerModel
from .network import Network
from .os import OS
from .software import Software
from .drive import Drive

__all__ = ["CloudServer"]


class CloudServer(_Base):
    __root_url = "https://api.timeweb.cloud/api/v1"
    __base_endpoint = f"{__root_url}/servers"
    __api_token: str

    id: int
    name: str
    comment: str
    creation_time: str
    os: OS
    software: Software | None
    preset_id: int | None
    location: str
    configurator_id: str | None
    boot_mode: str
    status: str
    start_time: str | None
    ddos_guard_enabled: bool
    support_ssh: bool
    is_dedicated_cpu: bool
    gpu: int
    cpu: int
    cpu_frequency: str
    ram: int
    drives: list[Drive]
    avatar_id: str | None
    vnc_pass: str
    root_pass: str | None
    image: Any
    networks: list[Network]
    cloud_init: str | None
    qemu_agent_enabled: bool
    availability_zone: str

    def __init__(self, api_token: str, **kwargs):
        validated_data = CloudServerModel(**kwargs).model_dump()
        super().__init__(api_token)

        self.id = validated_data["id"]
        self.name = validated_data["name"]
        self.comment = validated_data["comment"]
        self.creation_time = validated_data["creation_time"]
        self.os = OS(**validated_data["os"])
        self.software = Software(**validated_data["software"]) if validated_data["software"] is not None else None
        self.preset_id = validated_data["preset_id"]
        self.location = validated_data["location"]
        self.configurator_id = validated_data["configurator_id"]
        self.boot_mode = validated_data["boot_mode"]
        self.status = validated_data["status"]
        self.start_time = validated_data["start_time"]
        self.ddos_guard_enabled = validated_data["ddos_guard_enabled"]
        self.support_ssh = validated_data["support_ssh"]
        self.is_dedicated_cpu = validated_data["is_dedicated_cpu"]
        self.gpu = validated_data["gpu"]
        self.cpu = validated_data["cpu"]
        self.cpu_frequency = validated_data["cpu_frequency"]
        self.ram = validated_data["ram"]
        self.drives = [Drive(**drive) for drive in validated_data["drives"]]
        self.avatar_id = validated_data["avatar_id"]
        self.vnc_pass = validated_data["vnc_pass"]
        self.root_pass = validated_data["root_pass"]
        self.image = validated_data["image"]
        is_image_mounted: bool
        self.networks = [Network(**network) for network in validated_data["networks"]]
        self.cloud_init = validated_data["cloud_init"]
        self.qemu_agent_enabled = validated_data["qemu_agent_enabled"]
        self.availability_zone = validated_data["availability_zone"]

    def shutdown(self):
        return self._make_request(
            "post",
            f"{self.__base_endpoint}/{self.id}/shutdown",
        )

    @deprecated("Deprecated! Use methods like ``shutdown``")
    def execute_server_action(
        self,
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
        self._make_request("post", f"{self.__base_endpoint}/{self.id}/action", data)
