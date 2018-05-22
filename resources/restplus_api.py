from flask_restplus import Api

api = Api(
    version='0.8.0',
    title='JWT Demo',
    description='Python Flask RestPlus powered APIs',
    contact_url=None,
    contact_email="paapadmin@gsk.com",
    security=None,
    default_mediatype='application/json',
    doc="/swagger"
    )