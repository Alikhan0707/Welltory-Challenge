from pydantic import BaseModel
from typing import List
from datetime import date


class XYData(BaseModel):
    date: date
    value: float


class CalculationData(BaseModel):
    x_data_type: str
    y_data_type: str
    x: List[XYData]
    y: List[XYData]


class UserData(BaseModel):
    user_id: int
    data: CalculationData
