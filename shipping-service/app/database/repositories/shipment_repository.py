from typing import List

from sqlalchemy import func, desc
from sqlalchemy.orm import Session

from app.database.dbo.models import Shipment as Shipment_DBO
from app.routers.dto.shipment import ShipmentCreate


def get_all(db: Session, skip: int, limit: int) -> List[Shipment_DBO]:
    limit = None if limit == -1 else limit
    return db.query(Shipment_DBO)\
        .order_by(desc(Shipment_DBO.id))\
        .offset(skip)\
        .limit(limit)\
        .all()


def get_count(db: Session) -> int:
    return db.query(func.count(Shipment_DBO.id)).scalar()


def _update_shipment_dbo(dbo: Shipment_DBO, shipment: ShipmentCreate):
    dbo.from_harbor = shipment.from_harbor
    dbo.to_harbor = shipment.to_harbor
    dbo.leave_date = shipment.leave_date
    dbo.arrival_date = shipment.arrival_date


def create(db: Session, shipment: ShipmentCreate) -> Shipment_DBO:
    dbo = Shipment_DBO()
    _update_shipment_dbo(dbo, shipment)
    db.add(dbo)
    db.commit()

    return dbo
