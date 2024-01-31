
import streamlit as st
from fpdf import FPDF

def generate_resume(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 12)
    for section, content in data.items():
        pdf.cell(200, 10, txt=section, ln=True, align='C')
        pdf.cell(200, 10, txt="", ln=True, align='C')
        for sub_section, info in content.items():
            pdf.cell(200, 10, txt=sub_section, ln=True, align='L')
            for key, value in info.items():
                pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align='L')
            pdf.cell(200, 10, txt="", ln=True, align='L')
    pdf.output("your_resume.pdf")

def main():
    st.title("Resume Maker")

    with st.expander("Basic Details"):
        name = st.text_input("Name")
        phone = st.text_input("Phone Number")
        gmail = st.text_input("Gmail")
        github = st.text_input("Github")
        linkedin = st.text_input("Linkedin")

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
                "Phone No": phone,
                "Gmail": gmail,
                "Github": github,
                "Linkedin": linkedin
            },
            "Education Details": {"Education": education_details},
            "Programming Skills": {"Programming Skills": programming_skills},
            "Areas of Interest": {"Areas of Interest": areas_of_interest},
            "Projects": {"Projects": projects},
            "Internship Details": {"Internship Details": internship_details},
            "Academic Certification": {"Academic Certification": academic_certification},
            "Extracurricular Activities": {"Extracurricular Activities": extracurricular_activities}
        }
        generate_resume(data)
        st.success("Your resume has been generated! Click the link below to download.")
        st.markdown("[Download Your Resume](./your_resume.pdf)")

if __name__ == "__main__":
    main()
