import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

st.title("BMI Calculator")
st.write("Enter your weight and height to calculate your BMI.")

html_path = Path(__file__).parent / "index.html"
html = html_path.read_text(encoding="utf-8-sig")

components.html(html, height=500, scrolling=True)
