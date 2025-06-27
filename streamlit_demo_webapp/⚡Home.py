#!/usr/bin/python

import streamlit as st
# import base64
# from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
# Book based emojis here: https://emojipedia.org/world-book-day/
# URL Link: http://MAA-5CG102BJXG:8502


# --- Page Config ---
st.set_page_config(
    page_title="KIX Home",
    page_icon=":zap:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# image = Image.open('C:\\Users\\sureraja\\Downloads\\Workspace\\Python\\KIX-QA\\streamlit_demo_webapp\\images\\kix-qa.jpg')
# st.sidebar.image(image, use_column_width=True)

# --- Use Local CSS ---
file_name = "style/style.css"
with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Header Section ---
with st.container():
    # st.title("KIX AIO Portal")
    st.subheader("KIX AIO Portal for EOD Reporting, WBR, Train Doc, Process Improvement Scripts, etc.")
    st.write("[Click Here](https://www.google.com)")
