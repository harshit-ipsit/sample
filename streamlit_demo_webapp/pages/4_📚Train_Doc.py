#!/usr/bin/python

import streamlit as st

# --- Page Config ---
st.set_page_config(
   page_title="Train Doc",
   page_icon=":books:",
   layout="wide",
   initial_sidebar_state="expanded",
)

# --- Use Local CSS ---
file_name = "style/style.css"
with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Train Doc")
st.write(st.experimental_user)
