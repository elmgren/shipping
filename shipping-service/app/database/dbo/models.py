from datetime import date
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

# Used by alembic when auto-generating migrations
Base = declarative_base()
metadata = Base.metadata


class Ship(Base):
    __tablename__ = 'ship'

    id: int = Column(Integer(), primary_key=True, nullable=False, unique=True, autoincrement=True)
    name: str = Column(String(), nullable=False)


class Port(Base):
    __tablename__ = 'port'

    id: int = Column(Integer(), primary_key=True, nullable=False, unique=True, autoincrement=True)
    name: str = Column(String(), nullable=False)
    port_code: str = Column(String(), nullable=False, unique=True)


class Shipment(Base):
    __tablename__ = 'shipment'

    id: int = Column(Integer(), autoincrement=True, nullable=False, primary_key=True, unique=True)
    from_port: int = Column(Integer(), ForeignKey('port.id'), nullable=False)
    to_port: int = Column(Integer(), ForeignKey('port.id'), nullable=False)
    leave_date: date = Column(Date(), nullable=False)
    arrival_date: date = Column(Date(), nullable=True)