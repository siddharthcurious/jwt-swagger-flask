from functools import wraps
import jwt
from flask import request
from flask import current_app as app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "X-API-KEY" in request.headers:
            token = request.headers["X-API-KEY"]
        if not token:
            return { "message": "Token is missing!" }, 403
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
        except:
            return { "message": "Token is missing or invalid" }, 403
        return f(*args, **kwargs)
    return decorated