from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.routers.dto.shipment import AllShipments, Shipment, ShipmentCreate
from app.routers.router_dependencies import get_db_session
from app.routers.services import shipment_service

router = APIRouter()


@router.get("",
            status_code=status.HTTP_200_OK,
            response_model=List[Shipment],
            summary="Get all shipments")
async def router_get_all(db: Session = Depends(get_db_session), skip: int = 0, limit: int = 10):
    return await shipment_service.get_all(db, skip, limit)


@router.post("",
             status_code=status.HTTP_201_CREATED,
             response_model=Shipment,
             summary="Create a shipment")
async def router_create_shipment(entry: ShipmentCreate, db: Session = Depends(get_db_session)):
    return await shipment_service.create(db, entry)
