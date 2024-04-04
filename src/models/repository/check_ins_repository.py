from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import Checkins
from sqlalchemy.exc import IntegrityError


class CheckInRepository:
    def insert_check_in(self, attendee_id):
        with db_connection_handler as database:
            try:
                check_in = (
                    Checkins(attendeeId = attendee_id)
                )
                database.session.add(check_in)
                database.session.commit()
                return attendee_id
            
            except IntegrityError:
                raise Exception('Participante já fez check in!')
            
            except Exception as exception:
                database.session.rollback()
                raise exception
