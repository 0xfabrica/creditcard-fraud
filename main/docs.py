import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.set_page_config(
        page_title="Documentación Modelo XGBoost - Predicción de Impagos",
        page_icon="📊"
    )
    show_documentation()

def show_documentation():
    st.title("📊 Documentación del Modelo de Predicción de Impagos de Tarjetas de Crédito")
    
    st.markdown("""
    ## Descripción del Proyecto
    Este documento detalla los resultados del modelo XGBoost entrenado con el conjunto de datos 
    'Default of Credit Card Clients Dataset' de Taiwán (2005) para predecir impagos en tarjetas de crédito.
    
    ## Métricas del Modelo

    ### Precisión General
    """)

    st.metric(label="Puntuación del Modelo", value="82.2%")

    st.markdown("### Métricas Detalladas por Clase")

    metricas = pd.DataFrame({
        'Clase': ['No Impago (0)', 'Impago (1)'],
        'Precisión': [0.84, 0.68],
        'Recall': [0.95, 0.34],
        'F1-Score': [0.89, 0.46],
        'Support': [7040, 1960]
    })
    
    st.dataframe(metricas)

    st.markdown("### Matriz de Confusión")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Verdaderos Negativos (VN)", "6,774")
        st.metric("Falsos Negativos (FN)", "1,390")
    with col2:
        st.metric("Falsos Positivos (FP)", "266")
        st.metric("Verdaderos Positivos (VP)", "570")

    st.markdown("""
    ### Principales Hallazgos
    1. El modelo tiene mejor rendimiento identificando casos de no impago (Clase 0)
    2. Alta precisión para casos de impago (0.68) pero baja sensibilidad (0.34)
    3. Existe desbalance de clases en el conjunto de datos (7,040 vs 1,960 muestras)

    ### Fortalezas del Modelo
    - Alta precisión para predicciones de no impago (95% de recall para Clase 0)
    - Buena precisión general del 82.2%

    ### Áreas de Mejora
    - Baja sensibilidad para casos de impago (solo 34% de impagos reales detectados)
    - El desbalance de clases podría estar afectando el rendimiento del modelo

    ### Recomendaciones
    1. Implementar técnicas de balanceo de clases
    2. Explorar ingeniería de características para mejorar la detección de impagos
    3. Evaluar enfoques de aprendizaje sensibles al costo
    """)