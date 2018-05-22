from pymongo import MongoClient
from pymongo import errors
from flask import current_app as app

def connect(MONGO_URI, SSLFLAG=False, SSLCERT=None):

    try:
        if SSLFLAG == True:
            mongo_client = MongoClient(MONGO_URI, ssl=SSLFLAG, ssl_ca_certs=SSLCERT)
            return mongo_client
        else:
            mongo_client = MongoClient(MONGO_URI)
            mongo_client.server_info()
            return mongo_client
    except errors.ServerSelectionTimeoutError as err:
        app.logger.debug("mongodb server might be not running")
        app.logger.debug(err)
    except errors.ConnectionFailure as err:
        app.logger.debug("mongodb server is unreachable")
        app.logger.debug(err)

