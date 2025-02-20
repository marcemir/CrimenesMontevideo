import pandas as pd
from utils.preprocessing import preprocess_data
import os

# Obtener la ruta base del proyecto (CrimenesMontevideo)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Cargar el archivo CSV en un DataFrame
csv_path = os.path.join(BASE_DIR,"CrimenesMontevideo", "Data", "processed", "delitos_mvd_final_sin_vd.csv")
print(f"Ruta del archivo CSV: {csv_path}")

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"No se encontró el archivo: {csv_path}")

df_prueba = pd.read_csv(csv_path)

# Preprocesar los datos
df_procesado = preprocess_data(df_prueba)

# Mostrar las primeras filas del DataFrame preprocesado
print(df_procesado.head())

