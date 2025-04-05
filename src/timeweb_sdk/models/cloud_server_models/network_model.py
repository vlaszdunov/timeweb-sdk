from pydantic import BaseModel, Field
from typing import List, Literal

__all__ = ["IPAddressModel", "NetworkModel"]


class IPAddressModel(BaseModel):
    type: Literal["ipv4", "ipv6"]
    ip: str
    ptr: str | None = Field(default=None)
    is_main: bool


class NetworkModel(BaseModel):
    id: str | None = Field(default=None)
    type: Literal["public", "local"]
    nat_mode: Literal["dnat_and_snat", "snat", "no_nat"] | None = Field(default=None)
    bandwidth: int = Field(default=None)
    ips: List[IPAddressModel]
    blocked_ports: List[int] = Field(default=None)
