from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/call-logs")
def get_call_logs():
    url = "https://www.tabbly.io/dashboard/agents/endpoints/call-logs-v2"

    params = {
        "api_key": "25877eee91ff232b",   # 🔴 replace
        "organization_id": "2853",  # 🔴 replace
        "limit": 50,
        "offset": 0
    }

    response = requests.get(url, params=params)
    return response.json()