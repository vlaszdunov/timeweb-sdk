from pydantic import BaseModel, Field

__all__ = ["SoftwareModel"]


class SoftwareModel(BaseModel):
    id: int = Field(default=None)
    name: str = Field(default=None)
