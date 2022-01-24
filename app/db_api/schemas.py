from typing import Any, List
from datetime import date

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


# Correlation table schemas
class CorrelationBase(BaseModel):
    value: float
    p_value: float


class CorrelationCreate(CorrelationBase):
    pass


class CorrelationUpdate(CorrelationBase):
    pass


class Correlation(CorrelationBase):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


# UserData table schemas
class UserDataBase(BaseModel):
    x_data_type: str
    y_data_type: str


class UserDataIn(UserDataBase):
    user_id: int


class UserDataOut(UserDataIn):
    correlation_data: Correlation

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


# User table schemas
class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class XYData(BaseModel):
    date: date
    value: float

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class CalculationData(BaseModel):
    x_data_type: str
    y_data_type: str
    x: List[XYData]
    y: List[XYData]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class DataFromUser(BaseModel):
    user_id: int
    data: CalculationData

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict