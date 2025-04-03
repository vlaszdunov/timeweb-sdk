from dataclasses import dataclass
from timeweb_sdk.models import SoftwareModel

__all__ = ["Software"]


@dataclass
class Software:
    id: int | None
    name: str | None

    def __init__(self, **kwargs):
        validated_data = SoftwareModel(**kwargs).model_dump()
        self.id = validated_data["id"]
        self.name = validated_data["name"]
