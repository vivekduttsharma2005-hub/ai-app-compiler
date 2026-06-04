import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"


def extract_intent(user_prompt):

    prompt = f"""
You are an AI Intent Extractor.

Convert the user request into JSON.

User Request:
{user_prompt}

Return ONLY valid JSON.

Example:

{{
    "app_name": "CRM",
    "features": [
        "login",
        "contacts",
        "dashboard"
    ]
}}
"""

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content