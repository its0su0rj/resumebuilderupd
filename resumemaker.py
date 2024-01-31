import os
import streamlit as st
from fpdf import FPDF

def generate_resume(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for section, content in data.items():
        pdf.cell(200, 10, txt=section, ln=True, align='C')
        pdf.cell(200, 10, txt="", ln=True, align='C')
        
        if isinstance(content, list):  # Handle list data types
            for line in content:
                pdf.cell(200, 10, txt=line, ln=True, align='L')
        else:
            pdf.multi_cell(200, 10, txt=content, align='L')
    
    output_path = "your_resume.pdf"  # Specify the file name
    pdf.output(output_path)
    return output_path  # Return the file name of the generated PDF

def main():
    st.title("Resume Maker")
    
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    gmail = st.text_input("Gmail")
    github = st.text_input("Github")
    
    education_details = st.text_area("Education Details")
    
    programming_skills = st.text_area("Programming Skills")
    
    areas_of_interest = st.text_area("Areas of Interest")
    
    projects = st.text_area("Projects")
    
    internship_details = st.text_area("Internship Details")
    
    academic_certification = st.text_area("Academic Certification")
    
    extracurricular_activities = st.text_area("Extracurricular Activities")
    
    if st.button("Generate Resume"):
        data = {
            "Basic Details": f"Name: {name}\nPhone Number: {phone}\nGmail: {gmail}\nGithub: {github}",
            "Education Details": education_details.splitlines(),
            "Programming Skills": programming_skills.splitlines(),
            "Areas of Interest": areas_of_interest.splitlines(),
            "Projects": projects.splitlines(),
            "Internship Details": internship_details.splitlines(),
            "Academic Certification": academic_certification.splitlines(),
            "Extracurricular Activities": extracurricular_activities.splitlines()
        }
        resume_path = generate_resume(data)
        st.success("Your resume has been generated! Click the link below to download.")
        st.markdown(f"[Download Your Resume](./{resume_path})")  # Use relative path

if __name__ == "__main__":
    main()
