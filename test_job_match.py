import requests

# Local FastAPI endpoint
URL = "http://127.0.0.1:8000/analyze-resume-with-job/"

# Read job description
with open("job_description.txt", "r", encoding="utf-8") as f:
    job_description = f.read()

# Read resume and keep it open during request
with open("resume.pdf", "rb") as resume_file:
    files = {
        "resume": ("resume.pdf", resume_file, "application/pdf"),
    }
    data = {
        "job_description": job_description
    }

    response = requests.post(URL, files=files, data=data)

    if response.ok:
        print("Match Analysis:\n")
        print(response.json())
    else:
        print("Error:", response.status_code)
        print(response.text)
