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



def generate_match_analysis(resume_text: str, job_description: str) -> dict:
    prompt = f"""
You are a career advisor AI. A user provided the following resume and job description.

--- RESUME ---
{resume_text}

--- JOB DESCRIPTION ---
{job_description}

Analyze how well the resume matches the job. Include:

1. Match Summary (1–2 sentences)
2. Key Strengths
3. Gaps / Weaknesses
4. Suggestions to Improve the Resume

Output the response in this JSON format:
{{
  "summary": "...",
  "strengths": ["..."],
  "weaknesses": ["..."],
  "suggestions": ["..."]
}}
"""
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are an expert career advisor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=1000
    )

    reply = response.choices[0].message.content

    try:
        import json
        return json.loads(reply)
    except:
        return {"raw_response": reply}
