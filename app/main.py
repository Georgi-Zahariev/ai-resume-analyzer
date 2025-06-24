from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from app.resume_parser import extract_text
from app.feedback_engine import generate_feedback, generate_match_analysis


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

    analysis = generate_match_analysis(resume_text, job_description)
    return {"match_analysis": analysis}
