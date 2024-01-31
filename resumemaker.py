import streamlit as st
from fpdf import FPDF

def generate_resume(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    
    for section, content in data.items():
        pdf.cell(200, 10, txt=section, ln=True, align='C')
        pdf.cell(200, 10, txt="", ln=True, align='C')
        if isinstance(content, list):  # Handle list data types
            for item in content:
                pdf.cell(200, 10, txt=item, ln=True, align='L')
        else:
            pdf.cell(200, 10, txt=content, ln=True, align='L')
    
    pdf.output("your_resume.pdf")

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
            "Basic Details": {
                "Name": name,
                "Phone Number": phone,
                "Gmail": gmail,
                "Github": github
            },
            "Education Details": education_details,
            "Programming Skills": programming_skills,
            "Areas of Interest": areas_of_interest,
            "Projects": projects,
            "Internship Details": internship_details,
            "Academic Certification": academic_certification,
            "Extracurricular Activities": extracurricular_activities
        }
        generate_resume(data)
        st.success("Your resume has been generated! Click the link below to download.")
        st.markdown("[Download Your Resume](./your_resume.pdf)")

if __name__ == "__main__":
    main()
