from ..extensions import db

class User(db.Document):
    name = db.StringField()
    age = db.IntField()
    likes = db.ListField()
