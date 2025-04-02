from dataclasses import dataclass
from timeweb_sdk.models.cloud_server_models.os_model import OSModel

__all__ = ["OS"]


@dataclass
class OS:
    id: int
    name: str
    version: str

    def __init__(self, **kwargs):
        validated_data = OSModel(**kwargs).model_dump()
        self.id = validated_data["id"]
        self.name = validated_data["name"]
        self.version = validated_data["version"]
