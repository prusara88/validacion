import streamlit as st
import pandas as pd

# URL directa a tu Google Sheets (formato CSV)
sheet_id = "11w7SOMV_D2wymsiuSCQ_ygvkODXevVjx-TcKzc8EcbU"
sheet_name = "Registro"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Cargar los datos
try:
    df = pd.read_csv(url, dtype=str)  # Fuerza a texto
    df['documento'] = df['documento'].astype(str).str.strip()
    df['documento'] = df['documento'].str.replace(r'\D', '', regex=True)  # Solo dígitos
except Exception as e:
    st.error("❌ No se pudo cargar la hoja de cálculo. Asegúrate de que tenga una columna 'documento'.")
    st.stop()

# Interfaz
st.title("🔍 Verificador de Lista")

documento = st.text_input("Ingresa tu número de documento:")

if documento:
    documento = documento.strip()
    documento = ''.join(filter(str.isdigit, documento))  # Eliminar puntos o caracteres raros

    if documento in df['documento'].values:
        st.success("✅ ¡Sí estás en la lista!")
    else:
        st.error("❌ No estás en la lista.")
