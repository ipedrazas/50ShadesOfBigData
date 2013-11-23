from mongoengine import *


class Story(Document):
    uid = IntField(primary_key=True)
    title = StringField()
    date = DateTimeField()
    url = URLField()
    author = StringField()
    category = StringField()
    text_opc = StringField()
    content = StringField()
    visits = IntField()
    num_votes = IntField()
    votes_average = DecimalField()
