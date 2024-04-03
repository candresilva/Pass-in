import pytest
from src.models.settings.connection import db_connection_handler
from .check_ins_repository import CheckInRepository

db_connection_handler.__connect_to_db__()

#@pytest.mark.skip(reason = "Já inserido. Não quero testar novamente")
def test_insert_check_in():
        attendee_id = "2nd attendee"
        check_ins_repository = CheckInRepository()
        response = check_ins_repository.insert_check_in(attendee_id)
        print (response)

