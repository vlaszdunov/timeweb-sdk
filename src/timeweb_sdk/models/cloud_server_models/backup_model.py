from typing import Literal

from pydantic import BaseModel

__all__ = ["BackupModel"]


class BackupModel(BaseModel):
    id: int
    name: str
    comment: str
    created_at: str
    status: Literal["precreate", "delete", "shutdown", "recover", "create", "fail", "done"]
    size: int
    type: Literal["manual", "auto"]
    progress: int
