# components/locust_runner.py
import json
import socket
import subprocess
import webbrowser
from urllib.parse import urlparse
from datetime import datetime
import requests
import streamlit as st
from base64 import b64encode
from utils.history import save_history_data


def run_locust_test(api_url, method, headers_input, json_body, num_users, spawn_rate, run_time,
                    auth_type=None, bearer_token=None, basic_username=None, basic_password=None):
    try:
        # --- Validations ---
        if not api_url.strip():
            raise ValueError("API Endpoint URL is required.")
        if method not in ["GET", "POST", "PUT", "DELETE"]:
            raise ValueError("Invalid HTTP Method selected.")
        if method in ["POST", "PUT"] and not json_body.strip():
            raise ValueError("Request Body is required for POST and PUT.")
        if not run_time.strip():
            raise ValueError("Run Time is required (e.g., 10s, 1m).")
        if num_users <= 0 or spawn_rate <= 0:
            raise ValueError("Users and Spawn Rate must be > 0.")

        # --- Build Headers ---
        headers = json.loads(headers_input or "{}")
        if auth_type == "Bearer Token" and bearer_token:
            headers["Authorization"] = f"Bearer {bearer_token}"
        elif auth_type == "Basic Auth" and basic_username and basic_password:
            encoded = b64encode(f"{basic_username}:{basic_password}".encode()).decode()
            headers["Authorization"] = f"Basic {encoded}"

        payload = json.loads(json_body or "{}")

        # --- Pre-check API Response ---
        st.subheader("📥 Pre-Test API Response")
        response = requests.request(method, api_url, headers=headers,
                                    json=payload if method in ["POST", "PUT", "DELETE"] else None,
                                    params=payload if method == "GET" else None)

        st.markdown(f"✅ **Status:** {response.status_code}")
        if "application/json" in response.headers.get("Content-Type", ""):
            try:
                st.json(response.json())
            except Exception:
                st.code(response.text)
        else:
            st.code(response.text)

        if response.status_code >= 400:
            st.error("❌ Not starting Locust: request failed.")
            return

        # --- Check if Locust is already running ---
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            if sock.connect_ex(("localhost", 8089)) == 0:
                st.warning("⚠️ Locust UI is already running at [localhost:8089](http://localhost:8089)")
                return

        # --- Parse URL ---
        parsed_url = urlparse(api_url)
        host = f"{parsed_url.scheme}://{parsed_url.netloc}"
        path = parsed_url.path

        # --- Save .env ---
        with open("locustfile/.env", "w") as f:
            f.write(f"LOCUST_HOST={host}\n")
            f.write(f"REQ_METHOD={method}\n")
            f.write(f"REQ_URL={path}\n")
            f.write(f"REQ_HEADERS='{json.dumps(headers)}'\n")
            f.write(f"REQ_PAYLOAD='{json.dumps(payload)}'\n")

        # --- Save locust_payload.json ---
        with open("locustfile/locust_payload.json", "w") as f:
            json.dump({
                "url": api_url,
                "method": method,
                "headers": headers,
                "body": payload
            }, f, indent=2)

        # --- Launch Locust ---
        command = [
            "locust",
            "--config", "locust.conf",
            "-u", str(num_users),
            "-r", str(spawn_rate),
            "--host", host
        ]
        subprocess.Popen(command, cwd="locustfile")
        webbrowser.open("http://localhost:8089")
        st.success("🚀 Locust test started! [Open Locust UI](http://localhost:8089)")

        # --- Save History ---
        save_history_data({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "url": api_url,
            "method": method,
            "headers": headers,
            "body": payload,
            "users": num_users,
            "spawn_rate": spawn_rate,
            "run_time": run_time,
            "status": "Locust test started",
            "auth_type": auth_type
        })

    except json.JSONDecodeError:
        st.error("❌ Invalid JSON in headers or body.")
    except ValueError as ve:
        st.error(f"❌ {str(ve)}")
    except RuntimeError as re:
        st.error(f"❌ {str(re)}")
    except Exception as e:
        st.error(f"❌ Unexpected Error: {str(e)}")
