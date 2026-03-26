from sqlalchemy import Column, ForeignKey, Integer, String
from db.database import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    player1_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    player2_id = Column(Integer, ForeignKey("players.id"), nullable=False)