from flask import jsonify
from flask_restful import Resource

from ..model.user import User

class UserResource(Resource):
    def get(self):
        user = User.objects(name="frank").get_or_404()
        return jsonify(result=user)

    def post(self):
        user = User(name="frank", age=19)
        user.likes = [
            "Michael J. Fox",
            "Christopher Lloyd"
        ]
        user.save()

        return {'status': 'create new one'}
    