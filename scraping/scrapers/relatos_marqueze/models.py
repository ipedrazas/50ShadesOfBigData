from mongoengine import *


class Story(Document):
    slug = StringField(primary_key=True)
    title = StringField()
    date = DateTimeField()
    month = IntField()
    year = IntField()
    url = URLField()
    author = StringField()
    content = StringField()
    num_votes = IntField()
    votes_average = DecimalField()
    categories = ListField(StringField())
    tags = ListField(StringField())
