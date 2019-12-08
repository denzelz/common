from flask_restful import Resource, fields, marshal_with, reqparse
import json
from rooms.resource import rooms
from flask import request, abort

rooms_structure = {'number': fields.Integer,
                   'level': fields.Integer,
                   'status': fields.String,
                   'price': fields.Float
                   }

room_parser = reqparse.RequestParser()
room_parser.add_argument('number', type=int)
room_parser.add_argument('status', type=str)
room_parser.add_argument('price', type=int)


class RoomsTool(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        if room_parser.parse_args().get('number'):
            return [room for room in rooms if room.number == room_parser.parse_args().get('number')]
        elif room_parser.parse_args().get('status'):
            return [room for room in rooms if room.status == room_parser.parse_args().get('status')]
        else:
            return rooms

    @marshal_with(rooms_structure)
    def post(self):
        room = json.loads(request.data)
        rooms.append(room)
        return 'ok', 200

    def delete(self, room_number):
        return [rooms.remove(room) for room in rooms if room.number == room_number]

    @marshal_with(rooms_structure)
    def patch(self, room_number):
        for room in rooms:
            if room.number == room_number:
                if room_parser.parse_args().get('status'):
                    room.status = room_parser.parse_args().get('status')
                if room_parser.parse_args().get('price'):
                    room.price = room_parser.parse_args().get('price')
                else:
                    return abort(404)
