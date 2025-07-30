# APerformance_Testing_Tool
💻 Running the App:
 streamlit run main.py


                     API-Performance_Testing_Tool/
                    ├── components/
                    │   ├── __init__.py
                    │   ├── api_request.py
                    │   ├── locust_runner.py
                    │   └── sidebar.py
                    │
                    ├── locustfile/
                    │   ├── .env
                    │   ├── __init__.py
                    │   ├── locust.conf
                    │   ├── locust_payload.json
                    │   └── locustfile.py
                    │
                    ├── utils/
                    │   ├── __init__.py
                    │   ├── env_writer.py
                    │   └── history.py
                    │
                    ├── venv/                     # Virtual environment (optional to include in repo)
                    │
                    ├── .env                      # Root-level environment file
                    ├── history_tibcoresponse.json
                    ├── install.bat
                    ├── main.py
                    ├── requirements.txt
                    ├── streamlit_requirements.txt
                    ├── ui.css


## 💡 Features

- ✅ Send **GET**, **POST**, **PUT**, **DELETE** requests
- ✅ Input custom headers and JSON body
- ✅ Supports **Bearer Token** and **Basic Auth**
- ✅ Run **Locust** performance test with parameters
- ✅ Request **history tracking**, **replay**, and **delete**
- ✅ Clean UI with `ui.css` overrides
- ✅ Modular and extensible codebase



### 1️⃣ Install dependencies

pip install -r requirements.txt
