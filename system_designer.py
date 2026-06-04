import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"


def design_system(intent_json):

    prompt = f"""
You are a Software Architect.

Intent:

{intent_json}

Generate architecture JSON.

Return ONLY JSON.

Format:

{{
    "entities": [],
    "roles": []
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