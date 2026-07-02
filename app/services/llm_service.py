import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load environment variables from .env file
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model= genai.GenerativeModel("gemini-3.5-flash")

def generate_documentation(prompt:str):
    response=model.generate_content(prompt)
    
    return response.text