from mongoengine import *
# from ..extensions import db

class Students(Document):
    name = StringField(default="")
     