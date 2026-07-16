import streamlit as st


def mostrar_panel(departamento=None):

    st.subheader("📍 Información")

    st.metric(
        "Departamento",
        departamento if departamento else "-"
    )

    st.metric(
        "Habitantes",
        "-"
    )

    st.metric(
        "Superficie",
        "-"
    )