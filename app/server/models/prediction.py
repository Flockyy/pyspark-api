from typing import Optional

from pydantic import BaseModel, Field


class PredictionSchema(BaseModel):
  mushroom: str = Field(...)
  edible: bool = Field(...)

  class Config:
    schema_extra = {
      "example": {
        "mushroom": "???",
        "edible": "1",
      }
    }

class UpdatePredictionModel(BaseModel):
  mushroom: Optional[str]
  edible: Optional[bool]

  class Config:
    schema_extra = {
      "example": {
        "mushroom": "???",
        "edible": "1",
      }
    }


def ResponseModel(data, message):
  return {
    "data": [data],
    "code": 200,
    "message": message,
  }


def ErrorResponseModel(error, code, message):
  return {"error": error, "code": code, "message": message}