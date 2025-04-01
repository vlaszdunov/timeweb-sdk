from pydantic import BaseModel, Field
from typing import List


class OSModel(BaseModel):
    id: int
    name: str
    version: str
