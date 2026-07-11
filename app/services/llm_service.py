import os
from dotenv import load_dotenv
from google import genai

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured")
client = genai.Client(api_key=api_key)

def generate_documentation(prompt:str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    if not response.text:
        raise RuntimeError("Gemini returned an empty response")

    return response.text