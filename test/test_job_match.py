import requests
from pathlib import Path

# File locations
resume_path = "sources/resume.pdf"                    
job_desc_path = "sources/job_description.txt" # Now correctly using subfolder
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

url = "http://localhost:8000/analyze-resume-with-job/"

# Read job description
with open(job_desc_path, "r", encoding="utf-8") as f:
    job_description = f.read()

# Send request with resume file and job description text
with open(resume_path, "rb") as resume_file:
    files = {
        "resume": ("resume.pdf", resume_file, "application/pdf"),
    }
    data = {
        "job_description": job_description
    }

    response = requests.post(url, files=files, data=data)

    result_file = results_dir / "result_job_match.txt"
    with open(result_file, "w", encoding="utf-8") as out:
        if response.ok:
            out.write(str(response.json()))
            print("Match analysis saved to:", result_file)
        else:
            out.write(response.text)
            print("Error - saved response to:", result_file)
