import pytest
from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository 

db_connection_handler.__connect_to_db__()

@pytest.mark.skip(reason = "Já inserido. Não quero testar novamente")
def test_insert_attendee():
        attendee_info = {
            "uuid" : "mais um",
            "name" : "Antonio Cesar",
            "email" : "antony@email.com",
            "event_id" : "2o participante"
        }
        attendee_repository = AttendeesRepository()
        response = attendee_repository.insert_attendee(attendee_info)
        print (response)

@pytest.mark.skip(reason = "Não quero testar agora")
def test_get_attendee_byID():
        attendee_id = "bombando"
        attendee_repository = AttendeesRepository()
        response = attendee_repository.get_attendee_byID(attendee_id)
        print(response)

#@pytest.mark.skip(reason = "Não quero testar agora")
def test_get_attendee_badge_byID():
        attendee_id = "bombando"
        attendee_repository = AttendeesRepository()
        response = attendee_repository.get_attendee_badge_byID(attendee_id)
        print(response)
