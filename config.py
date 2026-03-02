import os
from dotenv import load_dotenv
from pathlib import Path

# Explicitly point to the .env file in the same directory as this script
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

# Debug: print the loaded values (remove these lines after confirming it works)
print("Loading .env from:", env_path)
print("BOT_TOKEN =", os.getenv("BOT_TOKEN"))
print("ADMIN_CHAT_ID =", os.getenv("ADMIN_CHAT_ID"))

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN is not set in environment variables")
    if not ADMIN_CHAT_ID:
        raise ValueError("ADMIN_CHAT_ID is not set in environment variables")

    try:
        ADMIN_CHAT_ID = int(ADMIN_CHAT_ID)
    except ValueError:
        raise ValueError("ADMIN_CHAT_ID must be an integer")

    RATE_LIMIT_SECONDS = 2