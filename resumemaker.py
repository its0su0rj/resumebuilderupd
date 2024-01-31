import streamlit as st
import base64

from fpdf import FPDF
from io import BytesIO


def get_binary_file_downloader_html(bin_data, file_label='File'):
    href = f'<a href="data:application/octet-stream;base64,{base64.b64encode(bin_data).decode()}" download="{file_label}.pdf">Download {file_label}</a>'
    return href

def generate_resume(data):
    pdf = FPDF()
    pdf.add_page()

    # Set font for headings
    pdf.set_font("Arial", style="B", size=12)

    # Add Basic Details
    pdf.cell(200, 10, txt="Basic Details:", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Name: {data['Basic Details']['Name']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Phone Number: {data['Basic Details']['Phone Number']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Gmail: {data['Basic Details']['Gmail']}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Github: {data['Basic Details']['Github']}", ln=True, align='L')

    # Add Education Details
    pdf.cell(200, 10, txt="\nEducation Details:", ln=True, align='L')
    pdf.multi_cell(200, 10, txt=data['Education Details'], align='L')

    # Add Programming Skills
    pdf.cell(200, 10, txt="\nProgramming Skills:", ln=True, align='L')
    pdf.multi_cell(200, 10, txt=data['Programming Skills'], align='L')

    # Add Areas of Interest
    pdf.cell(200, 10, txt="\nAreas of Interest:", ln=True, align='L')
    pdf.multi_cell(200, 10, txt=data['Areas of Interest'], align='L')

    # Add Projects
    pdf.cell(200, 10, txt="\nProjects:", ln=True, align='L')
    pdf.multi_cell(200, 10, txt=data['Projects'], align='L')

    # Add Internship Details
    pdf.cell(200, 10, txt="\nInternship Details:", ln=True, align='L')
    pdf.multi_cell(200, 10, txt=data['Internship Details'], align='L')

    # Add Academic Certification
    pdf.cell(200, 10, txt="\nAcademic Certification:", ln=True, align='L')
    pdf.multi_cell(200, 10, txt=data['Academic Certification'], align='L')

    # Add Extracurricular Activities
    pdf.cell(200, 10, txt="\nExtracurricular Activities:", ln=True, align='L')
    pdf.multi_cell(200, 10, txt=data['Extracurricular Activities'], align='L')

    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_data = pdf_output.getvalue().encode('latin-1', 'ignore')  # Encoding as UTF-8
    pdf_output.close()
    return pdf_data


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
        resume_data = generate_resume(data)
        st.success("Your resume has been generated! Click the link below to download.")
        st.markdown(get_binary_file_downloader_html(resume_data, "Resume PDF"), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
