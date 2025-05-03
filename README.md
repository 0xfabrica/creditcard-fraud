# Sistema de Predicción de Morosidad en Tarjetas de Crédito

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-v1.24.0-brightgreen)](https://streamlit.io/)
[![XGBoost](https://img.shields.io/badge/XGBoost-v1.7.5-orange)](https://xgboost.readthedocs.io/en/stable/)
[![Status: Stable](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](https://opensource.org/licenses/MIT)

## 📋 Descripción
Sistema de predicción de morosidad en tarjetas de crédito basado en Machine Learning, utilizando el conjunto de datos "Default of Credit Card Clients Dataset" de Taiwán (2005) y XGBoost para las predicciones.

## ✨ Características
- 🌐 Interfaz web interactiva (Streamlit)
- 🤖 Modelo XGBoost preentrenado
- ⚡ Predicción en tiempo real
- 📊 Visualización de resultados
- 📝 Documentación detallada
- 👥 Procesamiento multi-cliente

## 📊 Métricas del Modelo
- Precisión general: 82.2%
- Métricas por clase:
  - No morosos (0): 84% precisión
  - Morosos (1): 68% precisión
- F1-Score promedio: 0.80

## 🛠️ Requisitos
```bash
Python 3.8+
streamlit==1.24.0
pandas==1.5.3
xgboost==1.7.5
```

## ⚙️ Instalación
# Clonar repositorio
```bash
git clone [https://github.com/0xfabrica/credit-card-default-prediction.git](https://github.com/tuusuario/credit-card-default-prediction.git)
```
# Navegar al directorio
```bash
cd credit-card-default-prediction
```
# Instalar dependencias
```bash
pip install -r requirements.txt
```
# 🚀 Uso
```bash
# Ejecutar aplicación
streamlit run main.py
```

# 📁 Estructura del Proyecto
```bash
credit-card-default-prediction/
│
├── main.py                 # Aplicación principal
├── docs.py                # Documentación del modelo
├── modelo_xgboost_cc.json # Modelo preentrenado
├── requirements.txt       # Dependencias
└── README.md             # Este archivo
```

# 📋 Variables del Modelo

Entrada (23 características):
- 💳 Límite de crédito
- 👤 Datos demográficos   - Edad   - Sexo   - Educación   - Estado civil
- 📅 Historial de pagos (6 meses)
- 💰 Montos de facturas (6 meses)
- 💸 Cantidades pagadas (6 meses)

# 🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor:

- Fork el repositorio
- Crea una rama (git checkout -b feature/mejora)
- Commit cambios (git commit -am 'Añadir mejora')
- Push a la rama (git push origin feature/mejora)
-Abre un Pull Request

# 📧 Contacto
👨‍💻 Desarrollador: 0xfabrica
📧 Email: izanfabrica2022@gmail.com
🌐 GitHub: @0xfabrica

# 🙏 Agradecimientos
- UCI Machine Learning Repository
- Universidad de California, Irvine
- Comunidad de Streamlit
