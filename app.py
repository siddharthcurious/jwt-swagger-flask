from flask import Flask, Blueprint, request
from flask import g
from common.database_utils import connect
from resources.restplus_api import api
from resources.api.login import ns as namespace_login
from resources.api.register import ns as namespace_register
from resources.api.registered_user import ns as namespace_registered


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

app = Flask(__name__)
api.init_app(app)
api.authorizations=authorizations
api.add_namespace(namespace_register)
api.add_namespace(namespace_login)
api.add_namespace(namespace_registered)

app.config["MONGO_URI"] = "mongodb://localhost:27017/"
app.config["SSLFLAG"] = False
app.config["SSLCERT"] = None
app.config["MONGO_DATABASE"] = "test"
app.config["SECRET_KEY"] = "themaninthemirroristherightpersontotalkto"


@app.before_request
def get_mongodb():
	mongodb_connect  = connect(app.config['MONGO_URI'], app.config['SSLFLAG'], app.config['SSLCERT'])
	g.mongo_connect  = mongodb_connect
	g.db = mongodb_connect[app.config['MONGO_DATABASE']]

if __name__ == "__main__":
	app.run(port=6001)