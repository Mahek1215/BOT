import gradio as gr
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader

# Function to generate resume PDF
def generate_resume(name, job_title, email, phone, address, website, skills, languages, profile, experience, education):
    file_name = f"{name.replace(' ', '_')}_Resume.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    
    # Header Section
    c.setFillColor(colors.darkblue)
    c.rect(0, 700, 600, 100, fill=True, stroke=False)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, 750, name.upper())
    c.setFont("Helvetica", 14)
    c.drawString(50, 730, job_title)
    
    # Contact Section
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 12)
    c.drawString(50, 690, f"📧 {email}")
    c.drawString(50, 670, f"📞 {phone}")
    c.drawString(50, 650, f"📍 {address}")
    c.drawString(50, 630, f"🌍 {website}")
    
    # Skills
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 600, "SKILLS")
    c.setFont("Helvetica", 12)
    c.drawString(50, 580, skills)
    
    # Languages
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 550, "LANGUAGES")
    c.setFont("Helvetica", 12)
    c.drawString(50, 530, languages)
    
    # Profile
    c.setFont("Helvetica-Bold", 14)
    c.drawString(250, 690, "PROFILE")
    c.setFont("Helvetica", 12)
    c.drawString(250, 670, profile[:90])  # Limited to one line for design
    
    # Work Experience
    c.setFont("Helvetica-Bold", 14)
    c.drawString(250, 630, "WORK EXPERIENCE")
    c.setFont("Helvetica", 12)
    c.drawString(250, 610, experience)
    
    # Education
    c.setFont("Helvetica-Bold", 14)
    c.drawString(250, 570, "EDUCATION")
    c.setFont("Helvetica", 12)
    c.drawString(250, 550, education)
    
    c.save()
    return file_name

# Gradio UI
def resume_ui():
    with gr.Blocks() as app:
        gr.Markdown("""<h2 style='text-align: center; color: #3498db;'>📄 Resume Builder</h2>""")
        
        name = gr.Textbox(label="📝 Full Name")
        job_title = gr.Textbox(label="💼 Job Title")
        email = gr.Textbox(label="📧 Email")
        phone = gr.Textbox(label="📞 Phone Number")
        address = gr.Textbox(label="📍 Address")
        website = gr.Textbox(label="🌍 Website (optional)")
        skills = gr.Textbox(label="💡 Skills (comma separated)")
        languages = gr.Textbox(label="🌎 Languages (comma separated)")
        profile = gr.Textbox(label="📝 Short Profile Summary")
        experience = gr.Textbox(label="💼 Work Experience (format: Company, Role, Duration)")
        education = gr.Textbox(label="🎓 Education (format: Degree, Institution, Year)")
        
        btn = gr.Button("Generate Resume", elem_id="generate_btn")
        output = gr.File(label="📥 Download Your Resume")
        
        btn.click(generate_resume, inputs=[name, job_title, email, phone, address, website, skills, languages, profile, experience, education], outputs=output)
    
    return app

resume_ui().launch()
