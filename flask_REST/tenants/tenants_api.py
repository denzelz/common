from flask_restful import Resource, fields, marshal_with, reqparse
from flask import abort

from tenants.resource import tenants

address_structure = {
        "city": fields.String,
        "street": fields.String
}


tenants_structure = {
    'name': fields.String,
    'passport_id': fields.String,
    'age': fields.Integer,
    'sex': fields.String,
    'address': fields.Nested(address_structure),
    'room_number': fields.String,
                   }
tenants_parser = reqparse.RequestParser()
tenants_parser.add_argument('passport_id')
tenants_parser.add_argument('sex')
tenants_parser.add_argument('room_number')


class TenantsTool(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        if tenants_parser.parse_args().get('passport_id'):
            return [tenant for tenant in tenants if tenant.passport_id == tenants_parser.parse_args().get('passport_id')]
        if tenants_parser.parse_args().get('sex'):
            return [tenant for tenant in tenants if tenant.name == tenants_parser.parse_args().get('sex')]
        else:
            return tenants

    def delete(self, passport_id):
        return [tenants.remove(tenant) for tenant in tenants if tenant.passport_id == passport_id]

    def patch(self, passport_id):
        for tenant in tenants:
            if tenant.passport_id == passport_id:
                if tenants_parser.parse_args().get('room_number'):
                    tenant.room_number = tenants_parser.parse_args().get('room_number')
                else:
                    return abort(404)

