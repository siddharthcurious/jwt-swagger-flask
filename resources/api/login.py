from flask_restplus import Resource
from flask import g
from resources.restplus_api import api
import jwt
import datetime
from flask import current_app as app

ns = api.namespace("login", description="Operation - Login related operations")

@ns.route("/<string:unique_id>/<string:password>")
@api.response(500, "user not registered")
@api.response(400, "incorrect credenatials or not registered")
class Login(Resource):
    @api.response(200, "Successfully logged in")
    def get(self, unique_id, password):
        coll = g.db.user_info
        cursor = coll.find({"unique_id": unique_id, "password":  password})

        if cursor.count() == 1:
            token = jwt.encode({"user": unique_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config["SECRET_KEY"])
            return {"token": token}, 200
        return {"message": "Could not logged in"}, 500





