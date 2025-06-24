import requests
from pathlib import Path

# File paths (resume is still in root)
resume_path = "sources/resume.pdf"
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

url = "http://localhost:8000/analyze-resume/"

with open(resume_path, "rb") as f:
    files = {"file": (resume_path, f, "application/pdf")}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)

result_file = results_dir / "result_basic.txt"
with open(result_file, "w", encoding="utf-8") as out:
    if response.ok:
        out.write(str(response.json()))
        print("Saved result to:", result_file)
    else:
        out.write(response.text)
        print("Error - saved error response to:", result_file)
