import requests
from pathlib import Path

resume_path = "sources/resume.pdf"
results_dir = Path("results")
results_dir.mkdir(exist_ok=True)

url = "http://localhost:8000/analyze-resume/"


def format_list(items):
    return "\n".join(f"- {item}" for item in items) if items else "_None_"


with open(resume_path, "rb") as f:
    files = {"file": (resume_path, f, "application/pdf")}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)

result_file = results_dir / "result_basic.md"
with open(result_file, "w", encoding="utf-8") as out:
    if response.ok:
        data = response.json()
        md = f"""# Resume Feedback

**Summary**  
{data['feedback'].get('summary', '')}

---

**Strengths**
{format_list(data['feedback'].get('strengths', []))}

---

**Weaknesses**
{format_list(data['feedback'].get('weaknesses', []))}

---

**Suggestions**
{format_list(data['feedback'].get('suggestions', []))}
"""
        out.write(md)
        print("Saved to:", result_file)
    else:
        out.write(f"## Error:\n\n{response.text}")
        print("Error saved to:", result_file)
