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
    [data-testid="stSidebarNav"] {
        background-image: url(https://w.amazon.com/rest/wikis/xwiki/s3files/file/logo-generic.png);
        background-repeat: no-repeat;
        padding-top: 10px;
        background-position: 20px 20px;
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
