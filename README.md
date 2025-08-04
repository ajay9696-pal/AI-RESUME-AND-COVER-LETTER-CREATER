




#  AI Resume & Cover Letter Creator 

This project is a "Streamlit web app" that uses "AI (LLaMA3 via Ollama)" to automatically generate professional, ATS-friendly "resumes" and "cover letters" in PDF format. Users can enter their information, and the app builds documents tailored to different career targets such as MNC, Startup, Academic, or Government jobs.

---

##  Features

- Generate custom resumes with personal, educational, and technical details
- Automatically create first-person, job-ready cover letters
- Clean, styled PDF output using FPDF
- Fast and interactive UI via Streamlit
- Supports career styling: Standard, MNC, Startup, Government, Academic

---

# Project Structure


project
*aj.py              --> Main Streamlit app
* pa.py               --> PDF generation logic (resume & cover letter)
* README.md           --> Project description
* requirements.txt    --> Dependencies (streamlit, fpdf, etc.)
* /venv               --> Virtual environment (not included in repo)

---

# How It Works

## `aj.py`

This file contains the Streamlit interface:

* Users enter their personal and academic details
* Prompts are crafted and sent to the `ollama.chat()` function (using LLaMA3)
* Generated responses are split into sections
* PDF is generated using functions from `pa.py`
* Streamlit shows download buttons

## `pa.py`

This module:

* Uses `fpdf` (classic version) to build styled PDF documents
* Implements a custom class `CanvaStylePDF` with:

  * Header bar
  * Light section backgrounds
  * Clean, aligned text
* Contains two main functions:

  * `generate_resume_pdf(...)`
  * `generate_cover_letter_pdf(...)`
* Also includes `clean_text()` function to sanitize Unicode characters that `fpdf` can't handle

---




# Dependencies

* streamlit
* fpdf
* ollama

---



