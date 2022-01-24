from typing import List

from fastapi import FastAPI, HTTPException, Depends

from app.db_api import models, crud, database, schemas, calculation

database.db.connect()
database.db.create_tables([models.User, models.UserData, models.Correlation])
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


@app.get('/correlation', response_model=schemas.UserDataOut, dependencies=[Depends(get_db)])
def correlation(user_id: int, x_data_type: str, y_data_type: str):
    data = crud.get_user_data(user_id=user_id,
                              x_data_type=x_data_type,
                              y_data_type=y_data_type)
    if not data:
        raise HTTPException(status_code=404, detail='Not found')
    return data


@app.post('/calculate/', response_model=schemas.UserDataOut, dependencies=[Depends(get_db)])
def calculate(data: schemas.DataFromUser):
    calc = calculation.CalculateCorr(data.data.x, data.data.y)
    value, p_value = calc.correlation()
    data_to = crud.create_user_data(data, value, p_value)
    return data_to


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
