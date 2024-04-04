from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.checkins_handler import CheckinsHandler

checkin_route_bp = Blueprint("checkin_route", __name__)

@checkin_route_bp.route("/attendees/<attendee_id>/checkin", methods = ["POST"])
def create_checkin(attendee_id):
    http_request = HttpRequest(params={"attendee_id": attendee_id})
    checkin_handler = CheckinsHandler()
    http_response = checkin_handler.registry(http_request)
    return jsonify(http_response.body), http_response.status_code
