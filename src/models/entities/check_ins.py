from src.models.settings.base import Base
from src.models.entities.attendees import Attendees
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

class Checkins(Base):
  __tablename__ = "check_ins"

  id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
  attendeeId = Column(String, ForeignKey("attendees.id"))
  created_at = Column(DateTime, server_default=func.current_timestamp())

  def __repr__(self):
    return f"Check_ins [attendeeId = {self.attendeeId}]"
