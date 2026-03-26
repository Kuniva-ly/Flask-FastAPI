from sqlalchemy import Column, DateTime, Integer, String
from db.database import Base
from datetime import datetime, timezone


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    match_type = Column(String, nullable=False)  
    participant_1_id = Column(Integer, nullable=False)
    participant_2_id = Column(Integer, nullable=False)
    score_1 = Column(Integer, nullable=False)
    score_2 = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False) 