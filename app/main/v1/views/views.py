from flask import jsonify
from flask_restful import Resource
from app.main.v1.models.models import User,UserSchema

class ViewUser(Resource):
    def get(self):
        user = User.query.first()
        user_schema = UserSchema()
        output = user_schema.dump(user)
        

        return jsonify({ 'user' : output})