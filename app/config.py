import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

ALLOWED_LANGUAGES = ["Tamil", "English", "Hindi", "Malayalam", "Telugu"]
