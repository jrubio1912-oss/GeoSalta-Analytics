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

    st_folium(
        mapa,
        height=MAP_HEIGHT,
        width=None,
    )

with col_panel:

    mostrar_panel()