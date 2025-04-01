from dataclasses import dataclass, Field
from typing import Literal

__all__ = ["IPAddress", "Network"]

from timeweb_sdk.models import IPAddressModel, NetworkModel


@dataclass
class IPAddress:
    type: Literal["ipv4", "ipv6"]
    ip: str
    ptr: str | None
    is_main: bool

    def __init__(self, **kwargs):
        validated_data = IPAddressModel(**kwargs).model_dump()
        self.ip = validated_data["ip"]
        self.ptr = validated_data["ptr"]
        self.is_main = validated_data["is_main"]
        self.type = validated_data["type"]


@dataclass
class Network:
    id: str
    type: str
    nat_mode: str | None
    bandwidth: int | None
    ips:list[IPAddress]|None
    ddos_guard_enabled: bool
    blocked_ports: list[int]

    def __init__(self, **kwargs):
        validated_data = NetworkModel(**kwargs).model_dump()
        self.id = validated_data["id"]
        self.type = validated_data["type"]
        self.nat_mode = validated_data["nat_mode"]
        self.bandwidth = validated_data["bandwidth"]
        self.ips=[IPAddress(**ips) for ips in kwargs["ips"]]
        self.ddos_guard_enabled = validated_data["ddos_guard_enabled"]
        self.blocked_ports = validated_data["blocked_ports"]
