import streamlit as st
from utils.datos import obtener_lista_departamentos


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
        
        municipio = st.selectbox(
            "Municipio",
            [
                "Todos"
            ]
        )

    return indicador, departamento, municipio