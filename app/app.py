from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    api_key = os.getenv("API_KEY", "No API Key Found")
    db_password = os.getenv("DB_PASSWORD", "No DB Password Found")
    return f"API Key: {api_key}<br>DB Password: {db_password}"

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=80)
