from fastapi import FastAPI, File, UploadFile
from resume_parser import extract_text
from feedback_engine import generate_feedback

app = FastAPI()

@app.post("/analyze-resume/")
async def analyze_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(file.filename, content)
    feedback = generate_feedback(text)
    return {"feedback": feedback}