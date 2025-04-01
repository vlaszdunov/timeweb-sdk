from pydantic import BaseModel

__all__ = ["ImageModel"]


class ImageModel(BaseModel):
    id: str
    name: str
    is_custom: bool
