from pydantic import BaseModel, Field
from typing import List


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
    ddos_guard_enabled: bool = Field(default=None, alias="is_ddos_guard")
    is_image_mounted: bool = Field(default=None)
    blocked_ports: List[int] = Field(default=None)
