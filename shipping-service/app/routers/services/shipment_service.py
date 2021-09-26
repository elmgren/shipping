from sqlalchemy.orm import Session

from app.database.repositories import shipment_repository
from app.routers.dto.shipment import ShipmentCreate


async def get_all(db: Session, skip: int, limit: int):
    return shipment_repository.get_all(db, skip, limit)


async def create(db: Session, shipment: ShipmentCreate):
    return shipment_repository.create(db, shipment)
