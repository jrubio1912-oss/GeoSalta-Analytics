import streamlit as st
from streamlit_folium import st_folium

from utils.estilos import cargar_estilos
from utils.mapa import crear_mapa

from components.header import mostrar_header
from components.sidebar import mostrar_sidebar
from components.panel import mostrar_panel
from config.config import *

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🗺️",
    layout="wide"
)

cargar_estilos()

mostrar_header()

mostrar_sidebar()

col_mapa, col_panel = st.columns([4, 1])

with col_mapa:

    mapa = crear_mapa()

    mapa_interactivo = st_folium(
        mapa,
        height=MAP_HEIGHT,
        width=None
    )

    departamento_seleccionado = None

    if mapa_interactivo.get("last_active_drawing"):

        departamento_seleccionado = (
            mapa_interactivo["last_active_drawing"]
            ["properties"]
            ["nombre"]
            .title()
        )


st.write(mapa_interactivo)

with col_panel:

    mostrar_panel(departamento_seleccionado)