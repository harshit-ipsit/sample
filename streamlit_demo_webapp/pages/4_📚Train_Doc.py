#!/usr/bin/python

import streamlit as st

# --- Page Config ---
st.set_page_config(
   page_title="Train Doc",
   page_icon=":books:",
   layout="wide",
   initial_sidebar_state="expanded",
)

# --- Inline Custom CSS ---
st.markdown("""
    <style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebarNav"] {
        background-image: url(https://w.amazon.com/rest/wikis/xwiki/s3files/file/logo-generic.png);
        background-repeat: no-repeat;
        padding-top: 10px;
        background-position: 20px 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Train Doc")
st.write(st.experimental_user)
