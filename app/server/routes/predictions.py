from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_prediction,
    delete_prediction,
    retrieve_prediction,
    retrieve_predictions,
    update_prediction,
)
from app.server.models.prediction import (
    ErrorResponseModel,
    ResponseModel,
    PredictionSchema,
    UpdatePredictionModel,
)

router = APIRouter()

@router.post("/", response_description="Prediction data added into the database")
async def add_prediction_data(prediction: PermissionError = Body(...)):
    prediction = jsonable_encoder(prediction)
    new_prediction =  await add_prediction(prediction)
    return ResponseModel(new_prediction, "Prediction added successfully.")