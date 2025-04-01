from pydantic import BaseModel, Field
from typing import List


class ImageModel(BaseModel):
    id: str
    name: str
    is_custom: bool
