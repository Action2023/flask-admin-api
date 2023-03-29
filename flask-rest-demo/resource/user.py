from flask import jsonify, request
from flask_restful import Resource

from ..model.user import User

class UserResource(Resource):
    def get(self, name):
        user = User.objects(name=name).get_or_404()
        return jsonify(result=user)

class UsersResource(Resource):

    def post(self):
        req = request.get_json(force=True)
        user = User(name=req['name'], age=req['age'])
        user.likes = [
            "Michael J. Fox",
            "Christopher Lloyd"
        ]
        print("new one is -->", user.name)
        user.save()

        return {'status': 'create new one'}
    