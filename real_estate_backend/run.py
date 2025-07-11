import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)
# ✅ Load .env file from the current directory
load_dotenv(dotenv_path=".env")

print("🔧 DATABASE_URL from .env:", os.getenv("DATABASE_URL"))

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


