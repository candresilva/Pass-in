import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.__connect_to_db__()

#@pytest.mark.skip(reason = "Já inserido. Não quero testar novamente")
def test_insert_event():
            event = {
                "uuid" : "2o participante",
                "title" : "rocketseat v2",
                "details" : "passin-application backend",
                "slug" : "decolando no foguete novamente",
                "maximum_attendees" : 250
                }
            event_repository = EventsRepository()
            response = event_repository.insert_event(event)
            print (response)

#@pytest.mark.skip(reason = "Não quero testar agora")
def test_get_event_byID():
        event_id = "2o participante"
        event_repository = EventsRepository()
        response = event_repository.get_event_byID(event_id)
        print(response)
