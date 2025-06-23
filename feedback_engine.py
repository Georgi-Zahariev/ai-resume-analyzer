import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
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
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": resume_text}
        ],
        temperature=0.7,
        max_tokens=800,
    )
    
    reply = response.choices[0].message.content
    
    try:
        import json
        return json.loads(reply)
    except:
        return {"raw_response": reply}
