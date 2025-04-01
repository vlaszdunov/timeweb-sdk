from dataclasses import dataclass
from timeweb_sdk.models import ImageModel
__all__=["Image"]

@dataclass
class Image:
    id: str
    name: str
    is_custom: bool

    def __init__(self, **kwargs):
        validated_data = ImageModel(**kwargs).model_dump()
        self.id = validated_data["id"]
        self.name = validated_data["name"]
        self.is_custom = validated_data["is_custom"]