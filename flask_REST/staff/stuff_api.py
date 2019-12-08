from flask_restful import Resource, fields, marshal_with, reqparse
from flask import abort

from staff.resource import staff

staff_structure = {'name': fields.String,
                   'passport_id': fields.String,
                   'position': fields.String,
                   'salary': fields.Float
                   }

staff_parser = reqparse.RequestParser()
staff_parser.add_argument('position')
staff_parser.add_argument('salary')


class StaffTool(Resource):
    @marshal_with(staff_structure)
    def get(self):
        if staff_parser.parse_args().get('position'):
            return [staffs for staffs in staff
                    if staffs.position == staff_parser.parse_args().get('position')]
        else:
            return staff

    @marshal_with(staff_structure)
    def patch(self, passport_id):
        for staffs in staff:
            if staffs.passport_id == passport_id:
                if staff_parser.parse_args().get('position'):
                    staffs.position = staff_parser.parse_args().get('position')
                if staff_parser.parse_args().get('salary'):
                    staffs.salary = staff_parser.parse_args().get('salary')
                else:
                    return abort(404)

    def delete(self, passport_id):
        return [staff.remove(staffs) for staffs in staff if staffs.passport_id == passport_id]
