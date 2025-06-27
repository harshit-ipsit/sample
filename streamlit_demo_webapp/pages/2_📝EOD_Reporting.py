#!/usr/bin/python

import streamlit as st
import requests
import json

# --- Page Config ---
st.set_page_config(
    page_title="EOD Reporting",
    page_icon=":memo:",
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

# --- App Title ---
st.title("EOD Reporting")

# --- Slack Message Function ---
def send_slack_message(webhook_url, message):
    payload = {
        "text": message  # Slack expects "text", not "Content"
    }
    
    try:
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            st.success("✅ Message sent successfully to Slack.")
        else:
            st.error(f"❌ Failed to send message. Status: {response.status_code}")
            st.text(response.text)
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# --- Button to Trigger Slack Message ---
if st.button("Send EOD Slack Notification"):
    slack_webhook_url = st.secrets["SLACK_WEBHOOK_URL"]
    slack_message = "@channel, Hello from Python EOD Reporting App!"
    send_slack_message(slack_webhook_url, slack_message)
