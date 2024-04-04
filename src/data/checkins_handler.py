from src.models.repository.check_ins_repository import CheckInRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class CheckinsHandler:
    def __init__(self) -> None:
        self.__checkins_repository = CheckInRepository()

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        params = http_request.params["attendee_id"]
        self.__checkins_repository.insert_check_in(params)

        return HttpResponse(
            body = None,
            status_code=201
        )
    
