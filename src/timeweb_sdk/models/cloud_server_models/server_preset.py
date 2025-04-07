from typing import Literal

from pydantic import BaseModel, Field

__all__ = ["ServerPresetModel"]


class ServerPresetModel(BaseModel):
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
    local_network_allowed: bool = Field(alias="is_allowed_local_network")
    tags: list[str]
