from typing import Any, Literal
from warnings import deprecated
from timeweb_sdk.managers._base import _Base
from timeweb_sdk.models import CloudServerModel


class CloudServer(_Base):
    __root_url = "https://api.timeweb.cloud/api/v1"
    __base_endpoint = f"{__root_url}/servers"
    __api_token: str

    id: int
    name: str
    comment: str
    creation_time: str
    os: Any
    software: Any
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
    disks: Any
    avatar_id: str | None
    vnc_pass: str
    root_pass: str | None
    image: Any
    networks: Any
    cloud_init: str | None
    qemu_agent_enabled: bool
    availability_zone: str

    def __init__(self, api_token: str, **kwargs):
        validated_data = CloudServerModel(**kwargs)
        super().__init__(api_token)
        self.__dict__.update(validated_data.model_dump())

    def shutdown_server(self):
        return self._make_request(
            "post",
            f"{self.__base_endpoint}/{self.id}/shutdown",
        )

    @deprecated("Deprecated! Use methods like ``shutdown_server``")
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
        return self._make_request("post", f"{self.__base_endpoint}/{self.id}/action", data)
