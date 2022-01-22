from contextvars import ContextVar

import peewee

DATABASE_NAME = 'welltory_app_test.db'
USERNAME = 'postgres'
PASSWORD = 'Aldabaran1'
HOST = '127.0.0.1'
PORT = 5432

db_state_default = {'closed': None, 'conn': None, 'ctx': None, 'transactions': None}
db_state = ContextVar('db_state', default=db_state_default)


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__('_state', db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.PostgresqlDatabase(DATABASE_NAME, user=USERNAME, password=PASSWORD, host=HOST)
db._state = PeeweeConnectionState()
