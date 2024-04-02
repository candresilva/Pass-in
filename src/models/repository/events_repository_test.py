from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.__connect_to_db__()

def test_insert_event():
        event = {
            "uuid" : "hello uuid",
            "title" : "rocketseat",
            "details" : "passin-application",
            "slug" : "decolando no foguete",
            "maximum_attendees" : 250
            }
        event_repository = EventsRepository()
        response = event_repository.insert_event(event)
        print (response)