from fastapi import FastAPI, File, UploadFile, Form
from resume_parser import extract_text
from feedback_engine import generate_feedback
from pydantic import BaseModel

app = FastAPI()

@app.post("/analyze-resume/")
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(file.filename, content)
    feedback = generate_feedback(text)
    return {"feedback": feedback}


@app.post("/analyze-resume-with-job/")
async def analyze_resume_with_job(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume_content = await resume.read()
    resume_text = extract_text(resume.filename, resume_content)

    from feedback_engine import generate_match_analysis
    analysis = generate_match_analysis(resume_text, job_description)
    return {"match_analysis": analysis}
