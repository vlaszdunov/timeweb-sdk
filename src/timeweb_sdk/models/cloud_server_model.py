from typing import List
from pydantic import BaseModel, Field


class OSModel(BaseModel):
    id: int
    name: str
    version: str


class SoftwareModel(BaseModel):
    id: int = Field(default=None)
    name: str = Field(default=None)


class DriveModel(BaseModel):
    id: int
    size: int
    used: int
    type: str
    is_mounted: bool
    is_system: bool
    system_name: str
    status: str


class IPAddressModel(BaseModel):
    type: str
    ip: str
    ptr: str | None = Field(default=None)
    is_main: bool


class NetworkModel(BaseModel):
    id: str | None = Field(default=None)
    type: str
    nat_mode: str = Field(default=None)
    bandwidth: int = Field(default=None)
    ips: List[IPAddressModel]
    ddos_guard_enabled: bool = Field(default=None,alias="is_ddos_guard")
    is_image_mounted: bool = Field(default=None)
    blocked_ports: List[int] = Field(default=None)


class ImageModel(BaseModel):
    id: str
    name: str
    is_custom: bool


class CloudServerModel(BaseModel):
    id: int
    name: str
    comment: str
    creation_time: str=Field(alias='created_at')
    os: OSModel
    software: SoftwareModel | None
    preset_id: int | None
    location: str
    configurator_id: int | None
    boot_mode: str
    status: str
    start_time: str | None=Field(alias="start_at")
    ddos_guard_enabled:bool=Field(alias="is_ddos_guard")
    support_ssh: bool = Field(alias="is_master_ssh")
    is_dedicated_cpu: bool
    gpu: int
    cpu: int
    cpu_frequency: str
    ram: int
    disks: List[DriveModel]
    avatar_id: str | None
    vnc_pass: str
    root_pass: str | None
    image: ImageModel | None
    networks: List[NetworkModel]
    cloud_init: str | None
    qemu_agent_enabled: bool = Field(alias="is_qemu_agent")
    availability_zone: str
