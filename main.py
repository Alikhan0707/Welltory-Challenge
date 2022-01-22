from typing import List

from fastapi import FastAPI, HTTPException, Depends
from post_data_models import UserData

from db_api import models, crud, database, schemas

database.db.connect()
database.db.create_tables([models.User, models.UserData])
database.db.close()

app = FastAPI()

sleep_time = 10


async def reset_db_state():
    database.db._state._state.set(database.db_state_default.copy())
    database.db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        database.db.connect()
        yield
    finally:
        if not database.db.is_closed():
            database.db.close()


@app.post('/users/', response_model=schemas.User, dependencies=[Depends(get_db)])
def create_user(user: schemas.UserCreate):
    db_user = crud.get_user_by_username(username=user.username)
    if db_user:
        raise HTTPException(status_code=404, detail='User already registered')
    return crud.user_create(user=user)


@app.get('/users/', response_model=List[schemas.User], dependencies=[Depends(get_db)])
def get_users():
    users = crud.get_users()
    if not users:
        raise HTTPException(status_code=404, detail='No registered users in DB')
    return users


@app.post('/users/{user_id}/data/', response_model=List[schemas.UserData], dependencies=[Depends(get_db)])
def create_user_data(user_id: int, user_data: schemas.UserDataCreate):
    return crud.create_userdata(user_id=user_id, user_data=user_data)


# @app.get('/users/{user_id}/data', response_model=List[schemas.UserData], dependencies=Depends(get_db))
# def get_userdata(user_id: int):
#     return crud.get_userdata(user_id=user_id)


@app.get('/correlation')
async def correlation(x_data_type: str, y_data_type: str, user_id: int):
    userdata = crud.get_userdata(user_id)
    if not userdata:
        raise HTTPException(status_code=404, detail='Not found')
    correlation_data = crud.get_correlation(userdata.id)


@app.post('/calculate')
async def calculate(data: UserData):
    return {'message': data}
