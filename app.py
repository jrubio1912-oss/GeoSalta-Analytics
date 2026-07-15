import streamlit as st

from streamlit_folium import st_folium

from utils.mapa import crear_mapa


st.set_page_config(
    page_title="GeoSalta Analytics",
    page_icon="🗺️",
    layout="wide"
)


st.title("🗺️ GeoSalta Analytics")

st.caption("Plataforma Inteligente de Análisis Territorial")


mapa = crear_mapa()

st_folium(
    mapa,
    width=1200,
    height=700
)