### **Crime Risk Prediction in Montevideo**  

Este proyecto se centra en el **desarrollo de un modelo de Machine Learning para predecir el riesgo de delitos en la ciudad de Montevideo, Uruguay**. Utilizando técnicas avanzadas de análisis de datos, ingeniería de características y optimización de modelos, se busca generar una herramienta que apoye la toma de decisiones estratégicas para mejorar la seguridad pública.  

---

#### **Objetivos del Proyecto**  

- **Predecir zonas de alto riesgo de delitos** utilizando datos históricos y variables socioeconómicas, climáticas y temporales.  
- **Optimizar recursos de patrullaje** mediante un enfoque basado en datos.  
- **Analizar patrones delictivos** para comprender mejor la dinámica del crimen en Montevideo.  

---

#### **Tecnologías y Herramientas** 

- **Lenguaje:** Python  
- **Análisis de Datos:** `pandas`, `numpy`  
- **Visualización:** `matplotlib`, `seaborn`  
- **Machine Learning:** `scikit-learn`, `XGBoost`, `Decision Trees`, `Random Forest`,`Naive Bayes`, `Logistic Regression`, `AdaBoost`  
- **Optimización de Modelos:** `Optuna` (hiperparámetros)  
- **Entorno de Desarrollo:** Jupyter Notebooks, Visual Studio Code  

---

#### **Pipeline del Proyecto**  

1. **Recolección de Datos:**  
   - Datos de crímenes históricos  
   - Variables climáticas  
   - Información socioeconómica por barrio  

2. **Limpieza y preparación de Datos (DataCleaning):**
    - Integración de datos de diferentes fuentes
    - Tratamiento de valores faltantes.
    - Transformación de variables.
    - Creación de nuevas variables

3. **Análisis Exploratorio de Datos (EDA):**  
   - Identificación de patrones delictivos  
   - Análisis de correlaciones  
   - Detección de outliers  

4. **Ingeniería de Características:**  
   - Encoding de variables categóricas  
   - Creación de nuevas variables (features)  
   - Análisis de importancia de variables  

5. **Modelado Predictivo:**  
   - Entrenamiento de modelos supervisados  
   - Optimización de hiperparámetros con Optuna  
   - Evaluación con métricas de rendimiento (AUC, F1-Score, Recall, Precision)  

6. **Evaluación del Modelo:**  
   - Análisis de la curva ROC 
   - Análisis del sobreajuste 
   - Optimización de umbral de clasificación  
   - Evaluación de métricas  

---

#### **Resultados Clave**  

- **Mejor Modelo:** Se obtuvo un modelo robusto con un AUC superior a 0.75 y un F1-Score optimizado mediante técnicas de ajuste de umbral.  
- **Optimización:** La utilización de **Optuna** permitió mejorar significativamente la performance del modelo ajustando hiperparámetros de manera eficiente.  

---

#### **Posibles Aplicaciones** 

- **Optimización de patrullajes**  
- **Análisis de zonas críticas para la seguridad pública**  
- **Apoyo en la planificación urbana y prevención del delito**  

---

#### **Skills Demostradas**  

- Análisis de datos complejos  
- Desarrollo de modelos de Machine Learning  
- Optimización de hiperparámetros con técnicas avanzadas  
