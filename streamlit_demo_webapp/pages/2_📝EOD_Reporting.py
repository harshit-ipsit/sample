#!/usr/bin/python

import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="EOD Reporting",
    page_icon=":memo:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Use Local CSS ---
file_name = "style/style.css"
with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("EOD Reporting")


