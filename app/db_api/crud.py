from . import models, schemas


def get_user_by_username(username: str):
    return models.User.filter(models.User.username == username).first()


def get_users():
    return list(models.User.select())


def user_create(user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password, email=user.email)
    db_user.save()
    return db_user


def get_user_data(user_id: int, x_data_type: str, y_data_type: str):
    db_user_data = models.UserData\
        .select()\
        .where((models.UserData.user_id == user_id) &
               (models.UserData.x_data_type == x_data_type) &
               (models.UserData.y_data_type == y_data_type))
    db_correlation = models.Correlation\
        .select(models.Correlation.value,
                models.Correlation.p_value)\
        .where(models.Correlation.user_data_id == db_user_data.first().id)

    db_data = db_user_data.dicts()[0]
    db_data['correlation_data'] = db_correlation.first()
    return db_data


def create_user_data(user_data: schemas.DataFromUser, value: float, p_value: float):

    db_user_data = models.UserData\
        .select()\
        .where((models.UserData.user_id == user_data.user_id) &
               (models.UserData.x_data_type == user_data.data.x_data_type) &
               (models.UserData.y_data_type == user_data.data.y_data_type))

    if db_user_data:
        models.Correlation\
            .update(user_data_id=db_user_data.first().id, value=value, p_value=p_value)\
            .where(models.Correlation.user_data_id == db_user_data.first().id)

        corr_data = models.Correlation\
            .select(models.Correlation.value, models.Correlation.p_value)\
            .where(models.Correlation.user_data_id == db_user_data.first().id)

        db_data = db_user_data.dicts()[0]
        db_data['correlation_data'] = corr_data.first()

        return db_data

    else:
        new_user_data = models.UserData.create(user_id=user_data.user_id,
                                               x_data_type=user_data.data.x_data_type,
                                               y_data_type=user_data.data.y_data_type)
        new_corr_data = models.Correlation.create(user_data_id=new_user_data.id, value=value, p_value=p_value)
        new_user_data.save()
        new_corr_data.save()

        db_user_data = models.UserData\
            .select()\
            .where((models.UserData.user_id == user_data.user_id) &
                   (models.UserData.x_data_type == user_data.data.x_data_type) &
                   (models.UserData.y_data_type == user_data.data.y_data_type))

        corr_data = models.Correlation \
            .select(models.Correlation.value, models.Correlation.p_value) \
            .where(models.Correlation.user_data_id == db_user_data.first().id)

        db_data = db_user_data.dicts()[0]
        db_data['correlation_data'] = corr_data.first()

        return db_data
