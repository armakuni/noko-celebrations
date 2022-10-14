from pydantic import BaseModel

from .users import NokoUser


class NokoEntry(BaseModel):
    id: int
    date: str
    minutes: int
    billable: bool
    user: NokoUser
