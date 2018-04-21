from mongoengine import *
class Picture_caption(Document):
    username = StringField()
    caption = StringField()
    picture = StringField()
    day = IntField()
