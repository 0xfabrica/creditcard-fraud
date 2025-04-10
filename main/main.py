import streamlit as st
import pandas as pd
import xgboost as xgb
import re
from docs import show_documentation

# Configuración de la página (DEBE SER LA PRIMERA LLAMADA A STREAMLIT)
st.set_page_config(
    page_title="Sistema de Predicción de Morosidad",
    layout="wide",
    page_icon="📊"
)

# Menú de navegación
menu = st.sidebar.selectbox(
    "Menú Principal",
    ["Predicción", "Documentación del Modelo"]
)

if menu == "Predicción":
    # Título de la aplicación
    st.title("Predicción de Morosidad con IA")
    
    st.markdown("""
    Esta aplicación utiliza un modelo de Machine Learning para predecir si un cliente caerá en morosidad.
    Introduce los datos en los campos proporcionados y haz clic en "Realizar Predicción" para obtener el resultado.
    """)

    # Cargar Modelo
    path = './main/modelo_xgboost_cc.json'
    modelo = xgb.XGBClassifier()
    modelo.load_model(path)

    # Sidebar: Captura de datos del cliente
    st.sidebar.header("Introduce los datos del cliente")

    # Función para extraer el número entre paréntesis en las opciones
    def extract_number(text):
        match = re.search(r'\((\d+)\)', text)
        if match:
            return int(match.group(1))
        return 0  # Valor predeterminado en caso de que no haya coincidencia

    def user_input_features():
        limit_bal = st.sidebar.slider("Límite de Crédito", min_value=0, max_value=1000000, value=200000, step=10000, key="limit_bal")
        sex = st.sidebar.selectbox("Sexo", options=["Masculino (1)", "Femenino (2)"], index=1, key="sexo")
        education = st.sidebar.selectbox("Educación", options=["Graduate School (1)", "University (2)", "High School (3)", "Others (4)"], index=1, key="educacion")
        marriage = st.sidebar.selectbox("Estado Civil", options=["Casado (1)", "Soltero (2)", "Otros (3)"], index=0, key="estado_civil")
        age = st.sidebar.slider("Edad", min_value=18, max_value=100, value=30, step=1, key="edad")
        pay_0 = st.sidebar.slider("Estado de Pago (Septiembre)", min_value=-2, max_value=8, value=0, key="pay_0")
        pay_2 = st.sidebar.slider("Estado de Pago (Agosto)", min_value=-2, max_value=8, value=0, key="pay_2")
        pay_3 = st.sidebar.slider("Estado de Pago (Julio)", min_value=-2, max_value=8, value=0, key="pay_3")
        pay_4 = st.sidebar.slider("Estado de Pago (Junio)", min_value=-2, max_value=8, value=0, key="pay_4")
        pay_5 = st.sidebar.slider("Estado de Pago (Mayo)", min_value=-2, max_value=8, value=0, key="pay_5")
        pay_6 = st.sidebar.slider("Estado de Pago (Abril)", min_value=-2, max_value=8, value=0, key="pay_6")
        bill_amt1 = st.sidebar.number_input("Monto Factura (Septiembre)", value=0, key="bill_amt1")
        bill_amt2 = st.sidebar.number_input("Monto Factura (Agosto)", value=0, key="bill_amt2")
        bill_amt3 = st.sidebar.number_input("Monto Factura (Julio)", value=0, key="bill_amt3")
        bill_amt4 = st.sidebar.number_input("Monto Factura (Junio)", value=0, key="bill_amt4")
        bill_amt5 = st.sidebar.number_input("Monto Factura (Mayo)", value=0, key="bill_amt5")
        bill_amt6 = st.sidebar.number_input("Monto Factura (Abril)", value=0, key="bill_amt6")
        pay_amt1 = st.sidebar.number_input("Monto Pagado (Septiembre)", value=0, key="pay_amt1")
        pay_amt2 = st.sidebar.number_input("Monto Pagado (Agosto)", value=0, key="pay_amt2")
        pay_amt3 = st.sidebar.number_input("Monto Pagado (Julio)", value=0, key="pay_amt3")
        pay_amt4 = st.sidebar.number_input("Monto Pagado (Junio)", value=0, key="pay_amt4")
        pay_amt5 = st.sidebar.number_input("Monto Pagado (Mayo)", value=0, key="pay_amt5")
        pay_amt6 = st.sidebar.number_input("Monto Pagado (Abril)", value=0, key="pay_amt6")

        # Crear un DataFrame con los datos del usuario
        data = {
            "LIMIT_BAL": limit_bal,
            "SEX": extract_number(sex),
            "EDUCATION": extract_number(education),
            "MARRIAGE": extract_number(marriage),
            "AGE": age,
            "PAY_0": pay_0,
            "PAY_2": pay_2,
            "PAY_3": pay_3,
            "PAY_4": pay_4,
            "PAY_5": pay_5,
            "PAY_6": pay_6,
            "BILL_AMT1": bill_amt1,
            "BILL_AMT2": bill_amt2,
            "BILL_AMT3": bill_amt3,
            "BILL_AMT4": bill_amt4,
            "BILL_AMT5": bill_amt5,
            "BILL_AMT6": bill_amt6,
            "PAY_AMT1": pay_amt1,
            "PAY_AMT2": pay_amt2,
            "PAY_AMT3": pay_amt3,
            "PAY_AMT4": pay_amt4,
            "PAY_AMT5": pay_amt5,
            "PAY_AMT6": pay_amt6,
        }
        return pd.DataFrame(data, index=[0])

    # Crear un DataFrame vacío para almacenar las entradas
    if 'input_data' not in st.session_state:
        st.session_state.input_data = pd.DataFrame(columns=[
            "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "PAY_0",
            "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6", "BILL_AMT1",
            "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6",
            "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"])

    # Estado del formulario en session_state
    if 'form_visible' not in st.session_state:
        st.session_state.form_visible = False

    # Botón para mostrar el formulario de datos
    if st.sidebar.button("Mostrar Formulario de Datos", key="show_form"):
        st.session_state.form_visible = not st.session_state.form_visible

    # Mostrar el formulario de datos solo si 'form_visible' es True
    if st.session_state.form_visible:
        input_df = user_input_features()
        st.session_state.input_data_temp = input_df

    # Botón para agregar los datos al DataFrame
    if st.sidebar.button("Agregar Datos", key="add_data"):
        if 'input_data_temp' in st.session_state:
            st.session_state.input_data = pd.concat([st.session_state.input_data, st.session_state.input_data_temp], ignore_index=True)
            st.session_state.input_data_temp = None  # Limpiar los datos temporales después de agregarlos

    # Mostrar los datos ingresados
    st.subheader("Datos Ingresados")
    st.write(st.session_state.input_data)

    # Opción para borrar una fila
    if not st.session_state.input_data.empty:
        row_to_delete = st.selectbox("Selecciona la fila para borrar:", range(len(st.session_state.input_data)), key="row_delete_selectbox")
        if st.button("Borrar Fila Seleccionada", key="delete_row"):
            if len(st.session_state.input_data) > 0:
                st.session_state.input_data = st.session_state.input_data.drop(row_to_delete).reset_index(drop=True)

    # Realizar la predicción al hacer clic en el botón
    if st.button("Realizar Predicción", key="predict"):
        if not st.session_state.input_data.empty:
            # Asegurarse de que los datos son numéricos
            st.session_state.input_data = st.session_state.input_data.apply(pd.to_numeric, errors='coerce')

            # Asegurar el orden correcto de las columnas
            expected_columns = [
                "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "PAY_0",
                "PAY_2", "PAY_3", "PAY_4", "PAY_5", "PAY_6", "BILL_AMT1",
                "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6",
                "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"
            ]
            try:
                input_df_for_prediction = st.session_state.input_data[expected_columns]
                prediccion = modelo.predict(input_df_for_prediction)

                # Mostrar el resultado
                st.subheader("Resultado de la Predicción")
                for i, prediction in enumerate(prediccion):
                    st.write(f"Predicción para el cliente {i+1}:")
                    if prediction == 1:
                        st.error("El cliente tiene alta probabilidad de ser moroso.")
                    else:
                        st.success("El cliente probablemente no será moroso.")
            except KeyError as e:
                st.error(f"Error: Falta la columna {e} en los datos ingresados. Asegúrate de haber ingresado todos los datos requeridos.")
            except Exception as e:
                st.error(f"Ocurrió un error durante la predicción: {e}")
        else:
            st.warning("Por favor, agrega algunos datos antes de realizar la predicción.")

elif menu == "Documentación del Modelo":
    show_documentation()  # Llamada a la nueva función de documentación
