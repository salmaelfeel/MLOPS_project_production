# Hand Gesture Recognition - Production Repository

This repository contains the production-ready code for serving the trained hand gesture recognition model and integrating it with a game frontend.

## 🚀 Project Overview
The goal is to deploy a machine learning model for hand gesture classification to control a maze game. The backend is built with FastAPI, containerized with Docker, and monitored with MLflow.

## 🏗️ Backend Architecture
- **API:** FastAPI for serving predictions.
- **Model:** Trained model loaded from research repo (RandomForest).
- **Monitoring:** MLflow for tracking metrics, Prometheus + Grafana for system monitoring.
- **Containerization:** Docker and docker-compose setup.
- **Deployment:** AWS or ClawCloud.

## 🔨 Setup Instructions
1. Clone the repo and install dependencies.
2. Activate virtual environment.
3. Run the FastAPI server.
4. Access the API at `http://localhost:8000`.

## 📈 Monitoring
- Monitors model accuracy, data integrity, and server health.
- Visualized through Grafana dashboards.

## 🚀 Deployment
- Dockerfile and docker-compose.yml provided.
