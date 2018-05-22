from flask_restplus import Resource
from flask_restplus import reqparse
from flask import g
from flask import current_app as app
from resources.restplus_api import api
from models.input_models import user_info
import json
from bson import json_util
from common.token_validator import token_required

ns = api.namespace("register", description="Operation - Registration related operations")

@api.response(500, "user registration failed")
@ns.route("/user")
class Register(Resource):
    @api.hide
    def get(self):
        pass

    @api.response(200, "Successfully user registered")
    @api.expect(user_info)
    @token_required
    @api.doc(security="apikey")
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("first_name", type=str, required=True, help="user first name")
        parser.add_argument("last_name", type=str, required=True, help="user last name")
        parser.add_argument("unique_id", type=str, required=True, help="user id")
        parser.add_argument("email_id", type=str, required=True, help="user email")
        parser.add_argument("password", type=str, required=True, help="user password")
        request_obj = parser.parse_args()

        coll = g.db.user_info
        cursor = coll.find({"unique_id": request_obj["unique_id"]})

        if cursor.count() >= 1:
            return "user already exits", 201

        try:
            request_id = str(coll.insert_one(request_obj).inserted_id)
        except Exception as ex:
            app.logger.debug(ex)
            return 'could not save the request into mongodb', 500
        return json.loads(json_util.dumps(request_obj))