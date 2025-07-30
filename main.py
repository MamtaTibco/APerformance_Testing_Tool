# main.py
import streamlit as st
import os
from utils.history import load_history_data, save_history_data
from components.sidebar import render_sidebar
from components.api_request import send_api_request
from components.locust_runner import run_locust_test

st.set_page_config(layout="wide", page_title=" API Tester")

# Load UI styles if present
if os.path.exists("ui.css"):
    with open("ui.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🚀 API Performance Testing Tool")

# Input fields
api_url = st.text_input("API Endpoint URL", placeholder="e.g., http://localhost:8000/api/resource")
method = st.selectbox("HTTP Method", ["GET", "POST", "PUT", "DELETE"])
headers_input = st.text_area("Headers (JSON)", value='{"Content-Type": "application/json"}')
json_body = st.text_area("Request Body (JSON)", placeholder='{"key": "value"}')

# Authentication section
st.markdown("### 🔐 Authentication")
auth_type = st.radio("Auth Type", ["None", "Bearer Token", "Basic Auth"])

bearer_token = st.text_input("Bearer Token", type="password") if auth_type == "Bearer Token" else None
basic_username = st.text_input("Username") if auth_type == "Basic Auth" else None
basic_password = st.text_input("Password", type="password") if auth_type == "Basic Auth" else None

# Locust test configuration
st.markdown("### 🐛 Locust Load Test Settings")
num_users = st.number_input("Number of Users", min_value=1, value=1)
spawn_rate = st.number_input("Spawn Rate (users/sec)", min_value=1, value=1)
run_time = st.text_input("Run Time (e.g., 10s, 1m)", value="10s")

# Sidebar for history
render_sidebar()

# Action buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Send Request"):
        send_api_request(
            api_url, method, headers_input, json_body,
            auth_type, bearer_token, basic_username, basic_password
        )

with col2:
    if st.button("Run Locust Test"):
        run_locust_test(
            api_url, method, headers_input, json_body,
            num_users, spawn_rate, run_time,
            auth_type, bearer_token, basic_username, basic_password
        )
