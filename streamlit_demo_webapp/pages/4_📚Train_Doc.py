#!/usr/bin/python

import streamlit as st
from quipclient import quip
import quipclient.quip

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

st.title("Train Doc")
st.write(st.experimental_user)

# --- Quip Client Setup using Secrets ---
try:
    access_token = st.secrets["quip"]["access_token"]
    base_url = st.secrets["quip"]["base_url"]
    tid = st.secrets["quip"]["thread_id"]

    client = quip.QuipClient(access_token=access_token, base_url=base_url)
    user = client.get_authenticated_user()  # Optional: Validate access
    sheet = client.get_first_spreadsheet(tid)
    sheet_json = client.parse_spreadsheet_contents(sheet)
    sheet_len = len(sheet_json)
except quipclient.quip.QuipError as e:
    st.error("Failed to connect to Quip. Check your token or VPN.")
    st.stop()

# --- UI Form to Collect Input ---
with st.form("Add User Info"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        emp_id = st.text_input("Emp ID", "6")
    with col2:
        name = st.text_input("Name", "Prabhu")
    with col3:
        alias = st.text_input("Alias", "pprbh")
    with col4:
        location = st.text_input("Location", "Chennai")

    submitted = st.form_submit_button("Add to Quip")

if submitted:
    try:
        client.add_to_spreadsheet(tid, [emp_id, name, alias, location])
        st.success(f"Added to Quip: {emp_id}, {name}, {alias}, {location}")
    except Exception as e:
        st.error(f"Failed to add data to Quip: {str(e)}")
🛠️
