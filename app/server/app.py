from fastapi import FastAPI
from app.server.routes.predictions import router as PredictionRouter

app = FastAPI()

app.include_router(PredictionRouter, tags=["Prediction"], prefix="/prediction")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
  