from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db_cofig import Base


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer(), primary_key=True)
    model = Column(String(50),  nullable=False)
    brand = Column(String(50), nullable=False)
    year = Column(DateTime(), nullable=False)

    def __repr__(self):
        return f'\n<id={self.id} model={self.model} brand={self.brand} year={self.year}>'

    def __str__(self):
        return f'<id={self.id} model={self.model} brand={self.brand} year={self.year}>'

