from typing import List

from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from app.database.dbo.models import Harbor as Port_DBO
from app.routers.dto.harbor import HarborCreate


def get_all(db: Session, skip: int, limit: int) -> List[Port_DBO]:
    limit = None if skip == -1 else limit
    return db.query(Port_DBO)\
        .order_by(desc(Port_DBO.id))\
        .offset(skip)\
        .limit(limit)\
        .all()


def get_count(db: Session) -> int:
    return db.query(func.count(Port_DBO.id)).scalar()


def _update_port_dbo(dbo: Port_DBO, port: HarborCreate):
    dbo.name = port.name
    dbo.harbor_code = port.harbor_code


def create(db: Session, port: HarborCreate) -> Port_DBO:
    dbo = Port_DBO()
    _update_port_dbo(dbo, port)
    db.add(dbo)
    db.commit()

    return dbo
