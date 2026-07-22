import streamlit as st
from utils.datos import (
    obtener_info_departamento,
    contar_municipios,
    listar_municipios
)


def mostrar_panel(departamento=None):

    st.subheader("📍 Información")

    if departamento is None:

        st.info("Seleccione un departamento en el mapa.")

        return

    info = obtener_info_departamento(departamento)

    if info is None:

        st.error("No se encontró información.")

        return

    st.metric("Departamento", info["nombre"])

    st.metric("Cabecera", info["cabecera"])

    st.metric("Código", info["codigo"])

    st.metric(
        "Municipios",
        contar_municipios(info["nombre"])
    )

    municipios = listar_municipios(info["nombre"])
    st.markdown("### 🏘 Municipios")

    for municipio in municipios:
        st.write(f"• {municipio}")

