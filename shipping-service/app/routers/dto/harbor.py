from datetime import datetime
from typing import List

from pydantic import BaseModel


class HarborBase(BaseModel):
    name: str
    harbor_code: str


class HarborCreate(HarborBase):
    pass


class Harbor(HarborBase):
    id: int
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True


class AllHarbors(BaseModel):
    result: List[Harbor]
    count: int
