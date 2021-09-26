from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.routers.dto.harbor import HarborCreate, Harbor
from app.routers.router_dependencies import get_db_session
from app.routers.services import harbor_service

router = APIRouter()


@router.get("",
            status_code=status.HTTP_200_OK,
            response_model=List[Harbor],
            summary="Get all harbors in the database")
async def router_get_all(db: Session = Depends(get_db_session), skip: int = 0, limit: int = 10):
    return await harbor_service.get_all(db, skip, limit)


@router.post("",
             status_code=status.HTTP_201_CREATED,
             response_model=Harbor,
             summary="Create a harbor")
async def router_create_harbor(entry: HarborCreate, db: Session = Depends(get_db_session)):
    return await harbor_service.create(db, entry)
