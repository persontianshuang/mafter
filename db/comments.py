from datetime import datetime

from mongoengine import *

from db.config import _MongoengineConnect

from db.sentences.sentence import Sentences

connect(_MongoengineConnect)

class Comments(Document):
    belongsto_sentence = ReferenceField((Sentences))#,dbref=True

    content = StringField(max_length=50)
    love = IntField()

    add_date = DateTimeField(default=datetime.now, required=True) #datetime.utcnow  datetime.now()

