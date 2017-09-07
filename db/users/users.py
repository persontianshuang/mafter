from mongoengine import *
from datetime import datetime

from db import config

connect(config._MongoengineConnect)

class Users(Document):
    meta = {'allow_inheritance': True}
    # user_name = StringField(required=True,unique=True,primary_key=True)
    user_name = StringField(required=True,unique=True)
    # email = EmailField(primary_key=False)
    date = DateTimeField(default=datetime.now, required=True)


def get_user(user):
    '''
    :param user: 用户名
    :return: user的实例
    '''
    if Users.objects(user_name=user):
        user_class = Users.objects(user_name=user)[0]
    else:
        user_class = Users(user_name=user)
        user_class.save()
    return user_class

# user = get_user('meng')
# print(user)
