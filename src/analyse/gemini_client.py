# src/analyze/gemini_client.py
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=API_KEY)

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# Create model instance (can be reused)
model = genai.GenerativeModel(MODEL_NAME)


