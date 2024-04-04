from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from src.models.entities.check_ins import Checkins

from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound


class AttendeesRepository:
    def insert_attendee(self, attendeesInfo: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                attendee = (
                    Attendees(
                        id = attendeesInfo.get("uuid"),
                        name = attendeesInfo.get("name"),
                        email = attendeesInfo.get("email"),
                        event_id = attendeesInfo.get("event_id")
                    )
                )
                database.session.add(attendee)
                database.session.commit()
                return attendeesInfo

            except IntegrityError:
                raise Exception("Participante já cadastrado!")

            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_attendee_byID(self, attendee_id: str) -> Attendees:
        with db_connection_handler as database:
            try:
                attendee = (
                    database.session
                    .query(Attendees)
                    .filter(Attendees.id == attendee_id)
                    .one()
                )
                return attendee
            except NoResultFound:
               return None

    def get_attendee_badge_byID(self, attendee_id: str) -> Attendees:
        with db_connection_handler as database:
            try:
                attendee = (
                    database.session
                    .query(Attendees)
                    .join(Events, Events.id==Attendees.event_id)
                    .filter(Attendees.id == attendee_id)
                    .with_entities(
                        Attendees.name,
                        Attendees.email,
                        Events.title
                        )
                    .one()
                )
                return attendee
            except NoResultFound:
                return None


    def get_attendees_by_eventID(self, event_id: str) -> List[Attendees]:
        with db_connection_handler as database:
            try:
                attendees = (
                    database.session
                    .query(Attendees)
                    .outerjoin(Checkins, Checkins.attendeeId==Attendees.id)
                    .filter(Attendees.event_id == event_id)
                    .with_entities(
                        Attendees.id,
                        Attendees.name,
                        Attendees.email,
                        Checkins.created_at.label("checkedinAt"),
                        Attendees.created_at.label("subscribedAt")
                        )
                    .all()
                )
                return attendees
            except NoResultFound:
                return None