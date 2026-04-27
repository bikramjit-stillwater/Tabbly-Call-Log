from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import requests
import os

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ UI route (MAIN PAGE)
@app.get("/", response_class=HTMLResponse)
def serve_ui():
    with open("index.html", "r") as f:
        return f.read()

# ✅ API route
@app.get("/call-logs")
def get_call_logs():
    url = "https://www.tabbly.io/dashboard/agents/endpoints/call-logs-v2"

    params = {
        "api_key": os.getenv("API_KEY"),
        "organization_id": os.getenv("ORG_ID"),
        "limit": 50,
        "offset": 0
    }

    response = requests.get(url, params=params)
    return response.json()
