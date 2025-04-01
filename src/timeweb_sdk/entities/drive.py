from dataclasses import dataclass
from timeweb_sdk.models import DriveModel
__all__ = ["Drive"]


@dataclass
class Drive:
    id: int
    size: int
    used: int
    type: str
    is_mounted: bool
    is_system: bool
    system_name: str
    status: str

    def __init__(self, **kwargs):
        validated_data = DriveModel(**kwargs).model_dump()
        self.id = validated_data["id"]
        self.size = validated_data["size"]
        self.used = validated_data["used"]
        self.type = validated_data["type"]
        self.is_mounted = validated_data["is_mounted"]
        self.is_system = validated_data["is_system"]
        self.system_name = validated_data["system_name"]
        self.status = validated_data["status"]
