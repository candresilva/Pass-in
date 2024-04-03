import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class AttendeeHandler:
    def __init__(self) -> None:
        self.__attendee_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        event_id = http_request.params["event_id"]
        event_attendees = self.__events_repository.count_attendees_byevent(event_id)

        if (event_attendees["Seats available"] <= 0):
            raise Exception("Evento Lotado!")
        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        self.__attendee_repository.insert_attendee(body)

        return HttpResponse(
            body = None,
            status_code=201          
        )
    
    def find_attendee_badge(self, http_request: HttpRequest) -> HttpResponse:
        try:
            params = http_request.params["attendee_id"]
            attendee_badge = self.__attendee_repository.get_attendee_badge_byID(params)

            return HttpResponse(
                body = {
                    "badge":{
                        "name": attendee_badge.name,
                        "email": attendee_badge.email,
                        "title": attendee_badge.title,
                            }
                        },
                status_code=200
            )
        except:
            raise Exception("Participante não encontrado")

