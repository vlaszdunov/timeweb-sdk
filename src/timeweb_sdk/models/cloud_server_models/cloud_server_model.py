from typing import List
from pydantic import BaseModel, Field
from .network_model import NetworkModel
from .drive_model import DriveModel
from .os_model import OSModel
from .software_model import SoftwareModel
from .image_model import ImageModel

__all__ = ["CloudServerModel"]


class CloudServerModel(BaseModel):
    id: int
    name: str
    comment: str
    creation_time: str = Field(alias="created_at")
    os: OSModel
    software: SoftwareModel | None
    preset_id: int | None
    location: str
    configurator_id: int | None
    boot_mode: str
    status: str
    start_time: str | None = Field(alias="start_at")
    ddos_guard_enabled: bool = Field(alias="is_ddos_guard")
    support_ssh: bool = Field(alias="is_master_ssh")
    is_dedicated_cpu: bool
    gpu: int
    cpu: int
    cpu_frequency: str
    ram: int
    drives: List[DriveModel] = Field(alias="disks")
    avatar_id: str | None
    vnc_pass: str
    root_pass: str | None
    image: ImageModel | None
    is_image_mounted: bool
    networks: List[NetworkModel]
    cloud_init: str | None
    qemu_agent_enabled: bool = Field(alias="is_qemu_agent")
    availability_zone: str
