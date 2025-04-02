from pydantic import BaseModel

__all__ = ["DriveModel"]


class DriveModel(BaseModel):
    id: int
    size: int
    used: int
    type: str
    is_mounted: bool
    is_system: bool
    system_name: str
    status: str
