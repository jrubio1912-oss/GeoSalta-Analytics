import streamlit as st
from streamlit_folium import st_folium

from utils.mapa import crear_mapa
from utils.estilos import cargar_estilos

st.set_page_config(
    page_title="GeoSalta Analytics",
    page_icon="🗺️",
    layout="wide"
)

cargar_estilos()

# ---------- Header ----------

st.markdown("""
# 🗺️ GeoSalta Analytics
### Plataforma Inteligente de Análisis Territorial para la Provincia de Salta
""")

st.divider()

# ---------- Sidebar ----------

with st.sidebar:

    st.header("⚙️ Filtros")

    indicador = st.selectbox(
        "Indicador",
        [
            "Población",
            "Empleo",
            "Turismo",
            "Salud",
            "Educación"
        ]
    )

    departamento = st.selectbox(
        "Departamento",
        [
            "Todos"
        ]
    )

    municipio = st.selectbox(
        "Municipio",
        [
            "Todos"
        ]
    )

# ---------- Layout ----------

col_mapa, col_info = st.columns([4, 1])

with col_mapa:

    mapa = crear_mapa()

    st_folium(
        mapa,
        width=None,
        height=700
    )

with col_info:

    st.subheader("Información")

    st.info(
        "Seleccione un departamento en el mapa."
    )