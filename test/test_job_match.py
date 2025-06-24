import requests
from pathlib import Path

URL = "http://127.0.0.1:8000/analyze-resume-with-job/"
job_desc_path = "sources/job_description.txt"
resume_path = "sources/resume.pdf"
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

def format_list(items):
    return "\n".join(f"- {item}" for item in items) if items else "_None_"


with open(job_desc_path, "r", encoding="utf-8") as f:
    job_description = f.read()

with open(resume_path, "rb") as resume_file:
    files = {
        "resume": ("resume.pdf", resume_file, "application/pdf"),
    }
    data = {
        "job_description": job_description
    }

    response = requests.post(URL, files=files, data=data)

    result_file = results_dir / "result_job_match.md"
    with open(result_file, "w", encoding="utf-8") as out:
        if response.ok:
            data = response.json()
            md = f"""# Resume Match Analysis

**Summary**  
{data['match_analysis'].get('summary', '')}

---

**Strengths**
{format_list(data['match_analysis'].get('strengths', []))}

---

**Weaknesses**
{format_list(data['match_analysis'].get('weaknesses', []))}

---

**Suggestions**
{format_list(data['match_analysis'].get('suggestions', []))}
"""
            out.write(md)
            print("Saved to:", result_file)
        else:
            out.write(f"## Error:\n\n{response.text}")
            print("Error saved to:", result_file)

