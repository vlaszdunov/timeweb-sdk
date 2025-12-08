from dataclasses import dataclass
from typing import Literal
from timeweb_sdk.models import ServerConfigModel


@dataclass
class Requirements:
    cpu_min: int
    cpu_step: int
    cpu_max: int
    ram_min: int
    ram_step: int
    ram_max: int
    drive_min: int
    drive_step: int
    drive_max: int
    network_bandwidth_min: int
    network_bandwidth_step: int
    network_bandwidth_max: int
    gpu_min: int | None
    gpu_step: int | None
    gpu_max: int | None


@dataclass
class Price:
    cpu: int
    ram: int
    drive: int
    bandwidth: int | None
    gpu: int | None


@dataclass
class ServerConfig:
    id: int
    drive_type: Literal["ssd", "nvme", "hdd"]
    cpu_frequency: str
    location: str
    is_allowed_local_network: bool
    tags: list[str] | None
    requirements: Requirements
    prices: Price | None

    def __init__(self, **kwargs):
        validated_data = ServerConfigModel(**kwargs).model_dump()
        self.id = validated_data["id"]
        self.drive_type = validated_data["drive_type"]
        self.cpu_frequency = validated_data["cpu_frequency"]
        self.location = validated_data["location"]
        self.is_allowed_local_network = validated_data["is_allowed_local_network"]
        self.tags = validated_data["tags"]
        self.requirements = Requirements(**validated_data["requirements"])
        self.prices = (
            Price(**validated_data["prices"])
            if validated_data["prices"] is not None
            else None
        )
