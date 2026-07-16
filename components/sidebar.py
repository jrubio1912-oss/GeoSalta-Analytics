import streamlit as st
from utils.datos import obtener_lista_departamentos
from utils.datos import (
    obtener_lista_departamentos,
    obtener_municipios_por_departamento
)


def mostrar_sidebar():

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

        departamentos = ["Todos"] + obtener_lista_departamentos()

        departamento = st.selectbox(
            "Departamento",
            departamentos
        )
        
        municipios = ["Todos"] + obtener_municipios_por_departamento(departamento)

        municipio = st.selectbox(
            "Municipio",
            municipios
        )
       
    return indicador, departamento, municipio


