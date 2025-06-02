from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the model
model = joblib.load("app/model/rf_model.pkl")  # Change if needed

# Define the input schema
class HandLandmarks(BaseModel):
    features: list  # List of 63 numbers (21 landmarks x, y, z)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Hand Gesture Recognition API!"}

@app.post("/predict")
def predict(landmarks: HandLandmarks):
    input_data = np.array(landmarks.features).reshape(1, -1)
    prediction = model.predict(input_data)
    return {"gesture": prediction[0]}
