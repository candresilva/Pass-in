from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Relationship
from sqlalchemy.sql import func

class Check_ins(Base):
  __tablename__ = "check_ins"

  id = Column(Integer, nullable=False, autoincrement=True)
  created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp)
  attendee_id = Column(String, nullable=False, ForeignKey=True)
  attendee = Relationship("attendee", back_populates="check_ins")
  