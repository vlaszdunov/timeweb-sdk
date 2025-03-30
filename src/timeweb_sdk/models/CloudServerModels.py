from typing import List
from pydantic import BaseModel, Field
from typing import Optional


class OS(BaseModel):
    id: int
    name: str
    version: str


class Software(BaseModel):
    id: int = Field(default=None)
    name: str = Field(default=None)


class Disk(BaseModel):
    id: int
    size: int
    used: int
    type: str
    is_mounted: bool
    is_system: bool
    system_name: str
    status: str


class IPAddress(BaseModel):
    type: str
    ip: str
    ptr: str | None = Field(default=None)
    is_main: bool


class Network(BaseModel):
    id: str | None = Field(default=None)
    type: str
    nat_mode: str = Field(default=None)
    bandwidth: int = Field(default=None)
    ips: List[IPAddress]
    is_ddos_guard: bool = Field(default=None)
    is_image_mounted: bool = Field(default=None)
    blocked_ports: List[int] = Field(default=None)


class Image(BaseModel):
    id: str
    name: str
    is_custom: bool


class CloudServerModel(BaseModel):
    id: int
    name: str
    comment: str
    created_at: str
    os: OS
    software: Software | None
    preset_id: int | None
    location: str
    configurator_id: int | None
    boot_mode: str
    status: str
    start_at: str | None
    is_ddos_guard: bool
    is_master_ssh: bool
    is_dedicated_cpu: bool
    gpu: int
    cpu: int
    cpu_frequency: str
    ram: int
    disks: List[Disk]
    avatar_id: str | None
    vnc_pass: str
    root_pass: str | None
    image: Image | None
    networks: List[Network]
    cloud_init: str | None
    is_qemu_agent: bool
    availability_zone: str
