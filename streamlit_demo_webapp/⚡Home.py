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
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Insert logo at the top of sidebar using ::before */
    [data-testid="stSidebarNav"]::before {
        content: "";
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 20px;
        height: 80px;
        width: 160px;
        background-image: url("https://w.amazon.com/rest/wikis/xwiki/s3files/file/logo-generic.png");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
with st.container():
    # st.title("AIO Portal")
    st.subheader("AIO Portal for EOD Reporting, WBR, Train Doc, Process Improvement Scripts, etc.")
    st.write("[Click Here](https://www.google.com)")
