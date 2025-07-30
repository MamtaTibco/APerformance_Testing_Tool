# components/api_request.py
import streamlit as st
import requests
import json
from datetime import datetime
from utils.history import save_history_data


def send_api_request(api_url, method, headers_input, json_body,
                     auth_type=None, bearer_token=None, basic_username=None, basic_password=None):
    try:
        # Parse headers and body safely
        headers = json.loads(headers_input or "{}")
        payload = json.loads(json_body or "{}")

        # Set authentication
        auth = None
        if auth_type == "Bearer Token" and bearer_token:
            headers["Authorization"] = f"Bearer {bearer_token}"
        elif auth_type == "Basic Auth" and basic_username and basic_password:
            auth = (basic_username, basic_password)

        # Send the request
        if method == "GET":
            response = requests.get(api_url, headers=headers, params=payload, auth=auth)
        elif method == "POST":
            response = requests.post(api_url, headers=headers, json=payload, auth=auth)
        elif method == "PUT":
            response = requests.put(api_url, headers=headers, json=payload, auth=auth)
        elif method == "DELETE":
            response = requests.delete(api_url, headers=headers, json=payload, auth=auth)
        else:
            st.error("❌ Unsupported HTTP method")
            return

        # Display the response
        st.subheader("📥 Response")
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            try:
                st.json(response.json())
            except Exception:
                st.code(response.text)
        else:
            st.code(response.text)

        # Save request/response to history
        save_history_data({
            "url": api_url,
            "method": method,
            "headers": headers,
            "body": payload,
            "status_code": response.status_code,
            "response": response.text,
            "auth_type": auth_type,
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        })

    except json.JSONDecodeError:
        st.error("❌ Invalid JSON format in headers or body.")
    except requests.RequestException as e:
        st.error(f"❌ Request error: {e}")
    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")
