from resources.restplus_api import api
from flask_restplus import fields

user_info = api.model("User Registration Info", {
    "first_name": fields.String(required=True),
    "last_name": fields.String(required=True),
    "unique_id": fields.String(required=True),
    "email_id": fields.String,
    "password": fields.String(required=True)
})