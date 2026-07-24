from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from app.database.database import Base


class Finance(Base):

    __tablename__ = "finance"

    id = Column(Integer, primary_key=True, index=True)

    month = Column(String, nullable=False)

    revenue = Column(Float)

    expenses = Column(Float)

    profit = Column(Float)