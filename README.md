# 📄 Resume Parser using Natural Language Processing (NLP)

This project is a Resume Parser built using Python and NLP techniques. It is designed to automatically extract structured data from resumes in various formats (PDF, DOCX). The goal is to streamline the candidate screening process by helping recruiters and HR systems extract and organize information like names, contact details, education, experience, and skills.

---

## 🧠 Project Objective

Recruiters often receive hundreds of resumes in different formats and layouts. Manually reviewing these resumes is time-consuming and prone to human error. This project solves that problem by automating the resume parsing process using Natural Language Processing (NLP). The parser extracts key fields and outputs them in a consistent, machine-readable format (e.g., JSON or CSV).

---


![Screenshot 2025-04-29 145834](https://github.com/user-attachments/assets/454683af-4c2f-45ef-972b-b1cf7797675e)


## 🚀 Features

- ✅ Extracts candidate details from unstructured text:
  - Name
  - Phone Number
  - Email Address
  - Education
  - Work Experience
  - Technical Skills
- ✅ Handles multiple resume formats (PDF and DOCX)
- ✅ Applies NLP techniques for improved accuracy
- ✅ Uses fallback logic to handle variations in formatting
- ✅ Outputs structured data for easy downstream use

---

## 🔧 Technologies & Libraries Used

| Tool/Library      | Purpose                                |
|-------------------|----------------------------------------|
| **Python**        | Programming language                   |
| **spaCy**         | NLP pipeline and Named Entity Recognition (NER) |
| **Regex (re)**    | Pattern matching for phone numbers, emails, etc. |
| **pdfminer.six**  | Extracting text from PDF resumes       |
| **docx2txt**      | Extracting text from DOCX resumes      |
| **nltk**          | Text preprocessing (optional)          |
| **pandas**        | Data storage and analysis              |
| **os, glob**      | File system operations                 |

---

## 🧪 Sample Input and Output

### 📥 Sample Resume File:
- Format: `PDF` or `DOCX`
- Content: Includes standard sections like Education, Work Experience, Skills, etc.

### 📤 Output (JSON):
```json
{
  "Name": "Hemanth Nagulu",
  "Email": "hemanth@email.com",
  "Phone": "+91-9876543210",
  "Skills": ["Python", "Machine Learning", "NLP", "SQL"],
  "Education": ["B.Tech in Computer Science - KL University (2020-2024)"],
  "Experience": ["AI Intern - XYZ Corp (Jan 2024 - Mar 2024)"]
}
