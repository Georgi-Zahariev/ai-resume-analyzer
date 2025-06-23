import requests

file_path = "resume.pdf"  # Change this to your filename
url = "http://localhost:8000/analyze-resume/"

with open(file_path, "rb") as f:
    files = {"file": (file_path, f, "application/pdf")}
    response = requests.post(url, files=files)

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())
