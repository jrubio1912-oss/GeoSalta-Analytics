from pathlib import Path
import streamlit as st


def cargar_estilos():
    css = Path("assets/styles.css").read_text(encoding="utf-8")

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True,
    )