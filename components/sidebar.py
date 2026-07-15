import streamlit as st


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

    return indicador, departamento, municipio