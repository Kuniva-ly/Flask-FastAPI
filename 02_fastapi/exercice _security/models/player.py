from sqlalchemy import Column, Integer, String
from db.database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, unique=True, nullable=False)
