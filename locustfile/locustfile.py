# locustfile/locustfile.py
from locust import HttpUser, task, between
import os
import json
from dotenv import load_dotenv

load_dotenv()


class APITestUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def perform_request(self):
        method = os.getenv("REQ_METHOD", "GET").upper()
        path = os.getenv("REQ_URL", "/")
        headers = json.loads(os.getenv("REQ_HEADERS", "{}"))
        payload = json.loads(os.getenv("REQ_PAYLOAD", "{}"))

        print(f"\n➡️ Sending {method} request to {path}")
        print(f"   Headers: {headers}")
        print(f"   Payload: {payload}")

        try:
            if method == "GET":
                self.client.get(path, headers=headers, params=payload, name=path)
            elif method == "POST":
                self.client.post(path, headers=headers, json=payload, name=path)
            elif method == "PUT":
                self.client.put(path, headers=headers, json=payload, name=path)
            elif method == "DELETE":
                self.client.delete(path, headers=headers, name=path)
            else:
                print(f"❌ Unsupported HTTP method: {method}")
        except Exception as e:
            print(f"❌ Request failed: {str(e)}")
