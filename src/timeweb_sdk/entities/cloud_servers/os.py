from dataclasses import dataclass
from timeweb_sdk.models import OSModel, OSRequirementsModel

__all__ = ["OS", "OSRequirements"]


@dataclass
class OSRequirements:
    cpu_min: int | None
    drive_min: int | None
    ram_min: int | None
    bandwidth_min: int | None

    def __init__(self, **kwargs):
        validated_data = OSRequirementsModel(**kwargs).model_dump()
        self.cpu_min = validated_data.get("cpu_min")
        self.drive_min = validated_data.get("disk_min")
        self.ram_min = validated_data.get("ram_min")
        self.bandwidth_min = validated_data.get("bandwidth_min")


@dataclass
class OS:
    id: int
    family: str | None
    name: str
    version: str
    version_codename: str | None
    description: str | None
    requirements: OSRequirements | None

    def __init__(self, **kwargs):
        validated_data = OSModel(**kwargs).model_dump()
        self.id = validated_data["id"]
        self.family = validated_data["family"]
        self.name = validated_data["name"]
        self.version = validated_data["version"]
        self.version_codename = validated_data["version_codename"]
        self.description = validated_data["description"]
        self.requirements = validated_data["requirements"]
        if self.requirements is not None:
            self.requirements = OSRequirements(**validated_data["requirements"])
