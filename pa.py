from fpdf import FPDF
import unicodedata

def clean_text(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')

class CanvaStylePDF(FPDF):
    def header(self):
        # Top header bar
        self.set_fill_color(120, 150, 255)  # Light blue
        self.rect(0, 0, 210, 20, 'F')
        self.set_font("Helvetica", 'B', 16)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, self.title_text, ln=1, align='C')
        self.ln(5)

    def add_section(self, title, content):
        self.set_text_color(0, 0, 0)
        self.set_font("Helvetica", 'B', 13)
        self.cell(0, 8, title, ln=1)
        self.set_font("Helvetica", '', 11)
        # Light background box
        self.set_fill_color(240, 240, 255)
        self.multi_cell(0, 6, clean_text(content), fill=True)
        self.ln(3)

def generate_resume_pdf(name, email, phone, linkedin, profile, education, projects, skills, soft_skills, extras):
    pdf = CanvaStylePDF()
    pdf.title_text = clean_text(name)
    pdf.add_page()

    # Contact info
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", '', 11)
    contact_line = f"Email: {email} | Phone: {phone}"
    if linkedin:
        contact_line += f" | LinkedIn: {linkedin}"
    pdf.cell(0, 8, clean_text(contact_line), ln=1, align='C')
    pdf.ln(4)

    # Sections
    pdf.add_section("Profile", profile)
    pdf.add_section("Education", education)
    pdf.add_section("Projects", projects)
    pdf.add_section("Technical Skills", skills)
    pdf.add_section("Soft Skills", soft_skills)
    pdf.add_section("Extra-Curricular", extras)

    file_path = "resume.pdf"
    pdf.output(file_path)
    return file_path

def generate_cover_letter_pdf(name, email, phone, linkedin, letter_text):
    pdf = CanvaStylePDF()
    pdf.title_text = clean_text(name)
    pdf.add_page()

    # Contact info
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Helvetica", '', 11)
    contact_line = f"Email: {email} | Phone: {phone}"
    if linkedin:
        contact_line += f" | LinkedIn: {linkedin}"
    pdf.cell(0, 8, clean_text(contact_line), ln=1, align='C')
    pdf.ln(5)

    # Letter body inside light background
    pdf.set_font("Helvetica", '', 12)
    pdf.set_fill_color(240, 240, 255)
    pdf.multi_cell(0, 7, clean_text(letter_text), fill=True)

    file_path = "cover_letter.pdf"
    pdf.output(file_path)
    return file_path