import streamlit as st
import pandas as pd

# Estilos para el botón
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #1E90FF;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-size: 16px;
    }
    div.stButton > button:hover {
        background-color: #0F78D1;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# URL de Google Sheets
sheet_id = "11w7SOMV_D2wymsiuSCQ_ygvkODXevVjx-TcKzc8EcbU"
sheet_name = "Registro"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Cargar los datos
try:
    df = pd.read_csv(url, dtype=str)
    df['documento'] = df['documento'].astype(str).str.strip()
    df['documento'] = df['documento'].str.replace(r'\D', '', regex=True)
except Exception as e:
    st.error("❌ No se pudo cargar la hoja de cálculo.")
    st.stop()

# Interfaz
st.title("🔍 Verificador de Lista")

documento = st.text_input("Ingresa tu número de documento:")

# Botón azul
if st.button("Buscar"):
    documento = documento.strip()
    documento = ''.join(filter(str.isdigit, documento))

    if documento in df['documento'].values:
        st.success("✅ ¡Sí estás en la lista!")
    else:
        st.error("❌ No estás en la lista.")
        st.markdown("👉 [Haz clic aquí para inscribirte](https://forms.gle/LuzAiCBWLnKSJwPN7)")
