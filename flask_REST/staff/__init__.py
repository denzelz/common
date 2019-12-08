from flask import Blueprint
from flask_restful import Api
from staff.stuff_api import StaffTool

staff_bp = Blueprint('staff', __name__)
api = Api(staff_bp)

api.add_resource(StaffTool, '/staff', '/staff/<passport_id>')
