from flask_restplus import Resource
from flask import g
from resources.restplus_api import api
from bson import json_util
import json
from common.token_validator import token_required

ns = api.namespace("registered", description="Operation - Registered user")

@ns.route("/user/<string:unique_id>")
@api.response(404, "user record not found")
class RegisteredUser(Resource):
    @api.response(200, "user record found")
    @token_required
    @api.doc(security='apikey')
    def get(self, unique_id):
        coll = g.db.user_info
        cursor = coll.find_one({"unique_id": unique_id})
        if cursor:
            return json.loads(json_util.dumps(cursor)), 200
        return {"message": "No such user record found"}, 404

@ns.route("/user/users")
@api.response(404, "users record not found")
class RegisteredUsers(Resource):
    @api.response(200, "users record found")
    @token_required
    @api.doc(security="apikey")
    def get(self):
        coll = g.db.user_info
        cursor = coll.find()
        users = []
        for user in cursor:
            user_information = json.loads(json_util.dumps(user))
            users.append(user_information)
        if len(users) == 0:
            return {"message": "users record not found"}, 404
        return users
