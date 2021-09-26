from datetime import date, datetime
from typing import List

from pydantic import BaseModel


class ShipmentBase(BaseModel):
    from_harbor: int
    to_harbor: int
    leave_date: date
    arrival_date: date


class ShipmentCreate(ShipmentBase):
    pass


class Shipment(ShipmentBase):
    id: int
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True


class AllShipments(BaseModel):
    result: List[Shipment]
    count: int
