# utils/env_writer.py
def write_env_file(host, method, path, headers, payload):
    with open(".env", "w") as f:
        f.write(f"LOCUST_HOST={host}\n")
        f.write(f"REQ_METHOD={method}\n")
        f.write(f"REQ_URL={path}\n")
        f.write(f"REQ_HEADERS='{headers}'\n")
        f.write(f"REQ_PAYLOAD='{payload}'\n")
