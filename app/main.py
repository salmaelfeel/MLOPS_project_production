from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://salmaelfeel.github.io",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

instrumentator = Instrumentator().instrument(app).expose(app)
