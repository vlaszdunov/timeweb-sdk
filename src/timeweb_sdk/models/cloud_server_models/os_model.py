from pydantic import BaseModel

__all__ = ["OSModel"]


class OSModel(BaseModel):
    id: int
    name: str
    version: str
