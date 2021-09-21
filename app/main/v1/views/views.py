
from flask_restful import Resource
from app.main.v1.models.models import User

class ViewUser(Resource):
    def get(self):
        return {
            'user': User.query.first().username
        }