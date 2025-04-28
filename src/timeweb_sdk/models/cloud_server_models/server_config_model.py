from pydantic import BaseModel, Field
from typing import Literal

__all__ = ["ServerConfigModel"]


class RequirementsModel(BaseModel):
    cpu_min: int
    cpu_step: int
    cpu_max: int
    ram_min: int
    ram_step: int
    ram_max: int
    drive_min: int = Field(alias="disk_min")
    drive_step: int = Field(alias="disk_step")
    drive_max: int = Field(alias="disk_max")
    network_bandwidth_min: int
    network_bandwidth_step: int
    network_bandwidth_max: int
    gpu_min: int | None
    gpu_step: int | None
    gpu_max: int | None


class PriceModel(BaseModel):
    cpu: int
    ram: int
    drive: int = Field(alias="disk")
    bandwidth: int | None
    gpu: int | None


class ServerConfigModel(BaseModel):
    id: int
    drive_type: Literal["ssd", "nvme", "hdd"] = Field(alias="disk_type")
    cpu_frequency: str
    location: str
    is_allowed_local_network: bool
    tags: list[str] | None = Field(default=None)
    requirements: RequirementsModel
    prices: PriceModel | None = Field(default=None)
