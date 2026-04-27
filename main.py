from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

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
        "api_key": os.getenv("API_KEY"),        # ✅ from Render
        "organization_id": os.getenv("ORG_ID"), # ✅ from Render
        "limit": 50,
        "offset": 0
    }

    response = requests.get(url, params=params)
    return response.json()
