from dataclasses import dataclass
from typing import Literal
from timeweb_sdk.models import ServerPresetModel

__all__ = ["ServerPreset"]


@dataclass()
class ServerPreset:
    id: int
    location: str
    price: int
    cpu: int
    cpu_frequency: str
    ram: int
    disk: int
    disk_type: Literal["ssd", "nvme", "hdd"]
    bandwidth: int
    description: str
    description_short: str
    local_network_allowed: bool
    tags: list[str]

    def __init__(self, **kwargs):
        validated_data = ServerPresetModel(**kwargs).model_dump()
        self.id = validated_data["id"]
        self.location = validated_data["location"]
        self.price = validated_data["price"]
        self.cpu = validated_data["cpu"]
        self.cpu_frequency = validated_data["cpu_frequency"]
        self.ram = validated_data["ram"]
        self.disk = validated_data["disk"]
        self.disk_type = validated_data["disk_type"]
        self.bandwidth = validated_data["bandwidth"]
        self.description = validated_data["description"]
        self.description_short = validated_data["description_short"]
        self.local_network_allowed = validated_data["local_network_allowed"]
        self.tags = validated_data["tags"]
