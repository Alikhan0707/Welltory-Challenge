import peewee

from .database import db


class User(peewee.Model):
    username = peewee.CharField(max_length=255, unique=True, index=True)
    password = peewee.CharField()
    email = peewee.CharField(max_length=255, unique=True, index=True)
    is_active = peewee.BooleanField(default=True)

    class Meta:
        database = db


class UserData(peewee.Model):
    user_id = peewee.ForeignKeyField(User, backref='user_data', on_delete='CASCADE')
    x_data_type = peewee.CharField()
    y_data_type = peewee.CharField()

    class Meta:
        database = db


class Correlation(peewee.Model):
    user_data_id = peewee.ForeignKeyField(UserData, backref='correlation', on_delete='CASCADE')
    value = peewee.FloatField()
    p_value = peewee.FloatField()

    class Meta:
        database = db
