from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pyspark.ml import PipelineModel
import pandas as pd

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
  SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# helpers

def student_helper(prediction) -> dict:
  return {
      "id": int(prediction["id"]),
      "mushroom": str(prediction["mushroom"]),
      "edible": bool(prediction["edible"]),
  }
  
# Retrieve all predictions present in the database
async def retrieve_predictions():
  pass

# Add a new prediction into to the database
async def add_prediction(prediction_data: dict) -> dict:
  model = PipelineModel().load('./../../model_decisiontree')
  # Pyspark df
  predict_df = pd.Dataframe(prediction_data)
  model.transform(predict_df)
  # Return prediction
  pass

# Retrieve a prediction with a matching ID
async def retrieve_prediction(id: int) -> dict:
  pass

# Update a prediction with a matching ID
async def update_prediction(id: int, data: dict):
  # Return false if an empty request body is sent.
  pass

# Delete a prediction from the database
async def delete_prediction(id: int):
  pass
