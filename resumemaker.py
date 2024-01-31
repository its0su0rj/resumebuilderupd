import streamlit as st
import base64

from fpdf import FPDF
from io import BytesIO


def get_binary_file_downloader_html(bin_file, file_label='File'):
    bin_file.seek(0)  # Reset the pointer to the beginning of the BytesIO object
    href = f'<a href="data:application/octet-stream;base64,{base64.b64encode(bin_file.read()).decode()}" download="{file_label}.pdf">Download {file_label}</a>'
    return href


def generate_resume(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for section, content in data.items():
        pdf.set_font("Arial", style='B', size=14)
        pdf.cell(200, 10, txt=section, ln=True, align='C')
        pdf.set_font("Arial", style='', size=12)
        
        if isinstance(content, list):  # Handle list data types
            for line in content:
                pdf.cell(200, 10, txt=line, ln=True, align='L')
        else:
            pdf.multi_cell(200, 10, txt=content, align='L')
    
    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest='S').encode('latin1'))
    pdf_output.seek(0)
    return pdf_output


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
            "Education Details": education_details,
            "Programming Skills": programming_skills,
            "Areas of Interest": areas_of_interest,
            "Projects": projects,
            "Internship Details": internship_details,
            "Academic Certification": academic_certification,
            "Extracurricular Activities": extracurricular_activities
        }
        resume_data = generate_resume(data)
        st.success("Your resume has been generated! Click the link below to download.")
        st.markdown(get_binary_file_downloader_html(resume_data, "Resume PDF"), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
