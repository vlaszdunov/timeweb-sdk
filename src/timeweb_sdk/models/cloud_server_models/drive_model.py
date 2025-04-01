from pydantic import BaseModel, Field
from typing import List


class DriveModel(BaseModel):
    id: int
    size: int
    used: int
    type: str
    is_mounted: bool
    is_system: bool
    system_name: str
    status: str
