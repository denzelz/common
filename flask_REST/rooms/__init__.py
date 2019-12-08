from flask import Blueprint
from flask_restful import Api
from rooms.rooms_api import RoomsTool

rooms_bp = Blueprint('rooms', __name__)
api = Api(rooms_bp)

api.add_resource(RoomsTool, '/rooms', '/rooms/<int:room_number>')
