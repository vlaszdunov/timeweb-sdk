from dataclasses import dataclass
from typing import Literal

@dataclass
class IPAddress:
    type: Literal["ipv4", "ipv6"]
    ip: str
    ptr: str | None
    is_main: bool


@dataclass
class Network:
    id: str
    type:Literal["public","local"]
    nat_mode:str|None
    bandwidth:int|None
    ips:list[IPAddress]
    ddos_guard_enabled:bool
    is_image_mounted: bool
    blocked_ports:list[int]