import os
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-pro")
