from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd

# Crear la app FastAPI
app = FastAPI(title="Crime Prediction API", description="API para predecir riesgo delictivo en Montevideo usando XGBoost")

# Cargar el modelo
model_path = "../Models/xgb_model.joblib"
model = joblib.load(model_path)

# Endpoint de prueba
@app.get("/")
def home():
    return {"message": "API de predicción de riesgo delictivo funcionando correctamente"}

# Endpoint para hacer predicciones
@app.post("/predict")
def predict(data: dict):
    try:
        # Convertir los datos de entrada en DataFrame
        input_data = pd.DataFrame([data])

        # Hacer predicción
        prediction = model.predict(input_data)

        # Retornar el resultado
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
