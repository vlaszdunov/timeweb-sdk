from pydantic import BaseModel, Field

__all__ = ["OSModel", "OSRequirementsModel"]


class OSRequirementsModel(BaseModel):
    cpu_min: int | None = Field(default=None)
    disk_min: int | None = Field(default=None)
    ram_min: int | None = Field(default=None)
    bandwidth_min: int | None = Field(default=None)


class OSModel(BaseModel):
    id: int
    family: str | None = Field(default=None)
    name: str
    version: str
    version_codename: str | None = Field(default=None)
    description: str | None = Field(default=None)
    requirements: OSRequirementsModel | None = Field(default=None)
