#!/usr/bin/python

import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Home",
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

    /* Sidebar Logo Styling */
    [data-testid="stSidebarNav"] {
        background-repeat: no-repeat;
        background-size: contain; /* Fit the logo without clipping */
        background-position: 20px 20px;
        padding-top: 100px;  /* Space for logo */
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Logo ---
with st.sidebar:
    st.image("logo-generic.png", use_column_width=True)

# --- Header Section ---
with st.container():
    # st.title("AIO Portal")
    st.subheader("AIO Portal for EOD Reporting, WBR, Train Doc, Process Improvement Scripts, etc.")
    st.write("[Click Here](https://www.google.com)")
