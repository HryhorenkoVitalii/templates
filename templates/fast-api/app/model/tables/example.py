from sqlalchemy import Column, DateTime, Integer, String

from .base import Base


class ExampleDatabase(Base):
    __tablename__ = "ExampleDatabase"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
