import json
import joblib
import pandas as pd
import os

# Obtener la ruta base del proyecto (CrimenesMontevideo)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))



# Cargar listas de variables desde el JSON
variables_path = os.path.join(BASE_DIR, "Models", "encoders", "variables.json")

# Comprobar si la ruta es correcta
if not os.path.exists(variables_path):
    raise FileNotFoundError(f"No se encontró el archivo: {variables_path}")
with open(variables_path, "r") as json_file:
    variables = json.load(json_file)

# Verificar que variables es una lista
if not isinstance(variables, list):
    raise TypeError("El archivo JSON debe contener una lista.")



# Cargar las 15 variables utilizadas en el modelo desde JSON
top_variables_path = os.path.join(BASE_DIR, "Models","encoders", "top_variables.json")

# Comprobar si la ruta es correcta
if not os.path.exists(top_variables_path):
    raise FileNotFoundError(f"No se encontró el archivo: {top_variables_path}")

with open(top_variables_path, "r") as json_file:
    top_variables = json.load(json_file)



# Cargar encoders y scaler entrenados
encoders_dir = os.path.join(BASE_DIR, "Models", "encoders")

one_hot_encoder = joblib.load(os.path.join(encoders_dir, "one_hot_encoder.joblib"))
target_encoder = joblib.load(os.path.join(encoders_dir, "target_encoder.joblib"))
woe_encoder = joblib.load(os.path.join(encoders_dir, "woe_encoder.joblib"))
scaler = joblib.load(os.path.join(encoders_dir, "scaler.joblib"))


# Función para preprocesar nuevos datos
def preprocess_data(df):
    """
    Preprocesa un nuevo conjunto de datos utilizando los encoders y el escalador entrenados.
    
    Parámetros:
    - df: DataFrame con las columnas sin procesar.

    Retorna:
    - df_encoded: DataFrame listo para ser usado en el modelo.
    """

    df_encoded = df.copy()

    # Seleccionar las variables utilizadas para preprocesar
    df_encoded = df_encoded[variables]
    
    
    # Aplicar target encoding a las columnas categóricas coreespondientes
    df_encoded = target_encoder.transform(df_encoded)
    
    # Aplicar standard scaling a las variables numéricas ESTE NO ANDA
    df_encoded = scaler.transform(df_encoded)
    
    # Aplicar one-hot encoding a las columnas categóricas correspondientes
    df_encoded = one_hot_encoder.transform(df_encoded)
    
    # Aplicar WOE encoding a las columnas categóricas
    df_encoded = woe_encoder.transform(df_encoded)
    
        
    # Seleccionar solamente las 15 variables utilizadas en el modelo
    df_encoded = df_encoded[top_variables]
    print(df_encoded.head())
    
    return df_encoded

'''
    # Aplicar Target Encoding
    df_encoded[targ_enc_columns] = target_encoder.transform(df_encoded[targ_enc_columns])

    # Aplicar One-Hot Encoding y convertir a DataFrame
    df_encoded = pd.DataFrame(one_hot_encoder.transform(df_encoded), columns=one_hot_encoder.get_feature_names_out())

    # Aplicar WOE Encoding y convertir a DataFrame
    df_encoded[woe_columns] = pd.DataFrame(woe_encoder.transform(df_encoded[woe_columns]), columns=woe_columns)

    # Aplicar Standard Scaling a variables numéricas
    df_encoded[continuous_columns] = scaler.transform(df_encoded[continuous_columns])
    
    # Seleccionar las 15 variables utilizadas en el modelo
    df_encoded = df_encoded[top_variables]

'''

