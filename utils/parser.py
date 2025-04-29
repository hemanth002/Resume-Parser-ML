import re
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_projects(text):
    project_blocks = re.findall(r"(?i)(project\s*title[:\-]?\s*)(.*?)(?=\n[A-Z][a-z]+:|\Z)", text, re.DOTALL)
    projects = []
    for _, block in project_blocks:
        lines = block.strip().split("\n")
        title = lines[0] if lines else ""
        desc = " ".join(lines[1:]) if len(lines) > 1 else ""
        tech = re.findall(r"(Python|Java|C\+\+|SQL|TensorFlow|Keras|React|Node\.js|Django|Flask)", desc, re.I)
        projects.append({
            "Title": title.strip(),
            "Description": desc.strip(),
            "Technologies": list(set(tech))
        })
    return projects

def extract_details(text):
    name = re.findall(r"Name[:\s]+([A-Z][a-z]+\s[A-Z][a-z]+)", text)
    email = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    phone = re.findall(r"\b\d{10}\b", text)
    skills = re.findall(r"Skills[:\s]+(.+)", text)
    education = re.findall(r"(B\.Tech|M\.Tech|BSc|MSc|PhD).+?\d{4}", text)
    projects = extract_projects(text)
    
    return {
        "Name": name[0] if name else "",
        "Email": email[0] if email else "",
        "Phone": phone[0] if phone else "",
        "Skills": skills[0].split(",") if skills else [],
        "Education": education,
        "Projects": projects
    }

def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    return extract_details(text)
