from flask import Blueprint
from flask_restful import Api

from tenants.tenants_api import TenantsTool

tenants_bp = Blueprint('tenants', __name__)
api = Api(tenants_bp)

api.add_resource(TenantsTool, '/tenants', '/tenants/<passport_id>')
