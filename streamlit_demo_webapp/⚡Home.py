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
    div[data-testid="stToolbar"] {visibility: hidden;}
    div[data-testid="stDecoration"] {visibility: hidden;}
    div[data-testid="stStatusWidget"] {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Logo ---
with st.sidebar:
    st.image(
        "https://w.amazon.com/rest/wikis/xwiki/s3files/file/logo-generic.png",
        use_container_width=True
    )

# --- Header Section ---
with st.container():
    # st.title("AIO Portal")
    st.subheader("AIO Portal for EOD Reporting, WBR, Train Doc, Process Improvement Scripts, etc.")
    st.write("[Click Here](https://www.google.com)")
