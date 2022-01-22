from . import models, schemas


def get_user_by_username(username: str):
    return models.User.filter(models.User.username == username).first()


def get_users():
    return list(models.User.select())


def user_create(user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password, email=user.email)
    db_user.save()


def get_user_data(user_id: int):
    return models.UserData.filter(models.UserData.user_id == user_id).first()


def create_user_data(user_id: int, user_data: schemas.UserDataCreate):
    db_user_data = models.UserData(**user_data.dict(), user_id=user_id)
    db_user_data.save()
    return db_user_data


def get_correlation(user_data_id: int):
    return models.Correlation.filter(models.Correlation.userdata_id == user_data_id).first()


def update_correlation(user_data_id: int, correlation_data: schemas.CorrelationUpdate):
    db_correlation = models.Correlation\
        .update(value=correlation_data.value, p_value=correlation_data.p_value)\
        .where(models.Correlation.userdata_id == user_data_id)
    db_correlation.save()
    return db_correlation
