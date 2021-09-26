from sqlalchemy.orm import Session

from app.database.repositories import harbor_repository
from app.routers.dto.harbor import HarborCreate


async def get_all(db: Session, skip: int, limit: int):
    return harbor_repository.get_all(db, skip, limit)


async def create(db: Session, port: HarborCreate):
    return harbor_repository.create(db, port)
