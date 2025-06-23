
import os
import openai
from dotenv import load_dotenv

load_dotenv()  # Load from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are a professional resume reviewer. Given a candidate's resume text, provide helpful, concise feedback:
- Highlight strong sections.
- Point out weak/improvable areas.
- Suggest relevant skills to add.
- Output response in JSON format:
  {
    "summary": "...",
    "strengths": [...],
    "weaknesses": [...],
    "suggestions": [...]
  }
"""

def generate_feedback(resume_text: str) -> dict:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": resume_text}
        ],
        temperature=0.7,
        max_tokens=800,
    )
    
    reply = response['choices'][0]['message']['content']
    
    try:
        # Parse it if model outputs valid JSON
        import json
        return json.loads(reply)
    except:
        # If not, return raw text
        return {"raw_response": reply}
