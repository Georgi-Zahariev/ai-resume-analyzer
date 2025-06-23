from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
import tempfile

def extract_text(filename: str, content: bytes) -> str:
    if filename.lower().endswith(".pdf"):
        return extract_from_pdf(content)
    elif filename.lower().endswith(".docx"):
        return extract_from_docx(content)
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are supported.")

def extract_from_pdf(content: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(content)
        temp_pdf.flush()
        text = extract_pdf_text(temp_pdf.name)
    return text.strip()

def extract_from_docx(content: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_docx:
        temp_docx.write(content)
        temp_docx.flush()
        doc = Document(temp_docx.name)
        text = "\n".join([p.text for p in doc.paragraphs])
    return text.strip()
