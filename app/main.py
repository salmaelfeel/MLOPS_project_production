from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the trained model
model = joblib.load("app/model/hand_gesture_model.pkl")

# Define input schema
class HandLandmarks(BaseModel):
    features: list  # 63 features (21 landmarks * x,y,z)

@app.post("/predict")
def predict(landmarks: HandLandmarks):
    input_features = np.array(landmarks.features).reshape(1, -1)
    prediction = model.predict(input_features)
    return {"gesture": prediction[0]}
