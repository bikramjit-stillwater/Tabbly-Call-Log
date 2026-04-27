from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# ✅ Allow frontend (important)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Root route (fixes "Not Found")
@app.get("/")
def home():
    return {"message": "Tabbly Call Logs API is running 🚀"}

# ✅ Call Logs API
@app.get("/call-logs")
def get_call_logs():
    url = "https://www.tabbly.io/dashboard/agents/endpoints/call-logs-v2"

    params = {
        "api_key": os.getenv("API_KEY"),        # from Render
        "organization_id": os.getenv("ORG_ID"), # from Render
        "limit": 50,
        "offset": 0
    }

    response = requests.get(url, params=params)

    # Debug safety
    try:
        return response.json()
    except:
        return {"error": "Failed to fetch logs", "raw": response.text}
