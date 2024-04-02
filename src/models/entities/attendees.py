from src.models.settings.base import Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import Relationship
from sqlalchemy.sql import func

class Attendees(Base):
  __tablename__ = "attendees"

  id = Column(String, primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False)
  event_id = Column(String, ForeignKey('events.id'), nullable=False)
  created_at = Column(DateTime, server_default = func.current_timestamp)
  event = Relationship("Events", back_populates="attendees")