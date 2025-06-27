#!/usr/bin/python

import streamlit as st
import os

# --- Page Config ---
st.set_page_config(
   page_title="Generate Test Accounts",
   page_icon=":rocket:",
   layout="wide",
   initial_sidebar_state="expanded",
)

# --- Use Local CSS ---
file_path = os.path.join(os.path.dirname(__file__), "style", "style.css")
with open(file_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Generate Test Accounts")
st.markdown("""---""")

