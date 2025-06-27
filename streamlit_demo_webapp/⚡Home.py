#!/usr/bin/python

import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="KIX Home",
    page_icon=":zap:",
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
        background-size: contain; /* Fit the logo without clipping */
        padding-top: 100px;  /* Space for logo */
        background-position: 20px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
with st.container():
    # st.title("AIO Portal")
    st.subheader("AIO Portal for EOD Reporting, WBR, Train Doc, Process Improvement Scripts, etc.")
    st.write("[Click Here](https://www.google.com)")
