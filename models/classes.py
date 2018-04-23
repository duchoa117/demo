from mongoengine import *


class Missions(Document):
    mission_name = StringField()
    description = StringField()



class User(Document):
    username = StringField(unique=True)
    email = StringField(unique= True)
    password = StringField()

class UserMission(Document):
    user =  ReferenceField(User)
    mission = ReferenceField(Missions)
    completed = BooleanField()
    image = StringField()
    caption = StringField()
