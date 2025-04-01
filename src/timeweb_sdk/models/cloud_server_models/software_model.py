from pydantic import BaseModel, Field
from typing import List


class SoftwareModel(BaseModel):
    id: int = Field(default=None)
    name: str = Field(default=None)
