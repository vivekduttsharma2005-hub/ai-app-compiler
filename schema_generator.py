import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"


def generate_schema(design_json):

    prompt = f"""
You are an Application Schema Generator.

Based on the architecture below, generate ONLY valid JSON.

Architecture:
{design_json}

Return exactly this format:

{{
    "ui_pages": [
        "Login",
        "Dashboard"
    ],
    "api_endpoints": [
        "/login",
        "/users"
    ],
    "database_tables": [
        "users",
        "roles"
    ]
}}

Do not include explanations.
Do not include markdown.
Do not wrap JSON inside ```json blocks.
Return JSON only.
"""

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return result