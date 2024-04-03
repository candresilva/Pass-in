import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)

        return HttpResponse(
            body = {"eventID": body["uuid"]},
            status_code=200          
        )
    
    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        try:
            params = http_request.params["event_id"]
            event = self.__events_repository.get_event_byID(params)
            event_attendees = self.__events_repository.count_attendees_byevent(params)

            return HttpResponse(
                body = {
                    "event":{
                        "id": event.id,
                        "title": event.title,
                        "details": event.details,
                        "slug": event.slug,
                        "maximum_attendees": event.maximum_attendees,
                        "attendees amount": event_attendees["Attendees amount"]
                            }
                        },
                status_code=200
            )
        except:
            raise Exception("Evento não encontrado")

