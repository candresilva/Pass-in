from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound


class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                event = Events(
                    id = eventsInfo.get("uuid"),
                    title = eventsInfo.get("title"),
                    details = eventsInfo.get("details"),
                    slug = eventsInfo.get("slug"),
                    maximum_attendees = eventsInfo.get("maximum_attendees"),
                )
                database.session.add(event)
                database.session.commit()
                return eventsInfo
            
            except IntegrityError:
                raise Exception('Evento já cadastrado!')
            
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_event_byID(self, event_id: str) -> Events:
        with db_connection_handler as database:
            try:
                event = (
                    database.session
                    .query(Events)
                    .filter(Events.id == event_id)
                    .one()
                )
                return event
            except NoResultFound:
                return None

    def count_attendees_byevent(self, event_id: str) -> Dict:
        with db_connection_handler as database:
            event_count = (
                database.session
                .query(Events)
                .join(Attendees, Events.id == Attendees.event_id)
                .filter(Events.id == event_id)
                .with_entities(
                    Events.maximum_attendees,
                    Attendees.id,
                )
                .all()
            )
            if len(event_count):
                return {
                    "Maximum attendees": event_count[0].maximum_attendees,
                    "Attendees amount": len(event_count),
                    "Seats available": (event_count[0].maximum_attendees- len(event_count))
                }
            else:
                return {
                    "Maximum attendees": 0,
                    "Attendees amount": 0,
                    "Seats available":"N/A"
                }