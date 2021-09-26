from datetime import date, datetime
from sqlalchemy import Column, String, Integer, ForeignKey, Date, func, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

# Used by alembic when auto-generating migrations
Base = declarative_base()
metadata = Base.metadata


class Ship(Base):
    __tablename__ = 'ship'

    id: int = Column(Integer(), primary_key=True, nullable=False, unique=True, autoincrement=True)
    name: str = Column(String(), nullable=False)
    created: datetime = Column(DateTime(), server_default=func.now(), nullable=False)
    updated: datetime = Column(DateTime(), server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)


class Harbor(Base):
    __tablename__ = 'harbor'

    id: int = Column(Integer(), primary_key=True, nullable=False, unique=True, autoincrement=True)
    name: str = Column(String(), nullable=False)
    harbor_code: str = Column(String(), nullable=False, unique=True)
    created: datetime = Column(DateTime(), server_default=func.now(), nullable=False)
    updated: datetime = Column(DateTime(), server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)


class Shipment(Base):
    __tablename__ = 'shipment'

    id: int = Column(Integer(), autoincrement=True, nullable=False, primary_key=True, unique=True)
    from_harbor: int = Column(Integer(), ForeignKey('harbor.id'), nullable=False)
    to_harbor: int = Column(Integer(), ForeignKey('harbor.id'), nullable=False)
    leave_date: date = Column(Date(), nullable=False)
    arrival_date: date = Column(Date(), nullable=True)
    created: datetime = Column(DateTime(), server_default=func.now(), nullable=False)
    updated: datetime = Column(DateTime(), server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

