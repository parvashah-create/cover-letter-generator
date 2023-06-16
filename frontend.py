# Import libraries
import streamlit as st

# Import functions
from data_sources import pdf_loader
from llm import cl_generator

# Set the title of the web application
st.title("Cover Letter Generator 📬")

# Get the OpenAI API key from the user
openai_key = st.text_input("Enter your OpenAi Key:")

st.write("https://openaimaster.com/how-to-get-openai-api-key-for-free/")

# Set the LLM temperature using a slider
temp = st.slider('Set LLM Temperature: Less Creative <<---------------->> More Creative', 0.0, 1.0, 0.5, 0.1)

# Allow the user to upload their resume in PDF format
upload_resume = st.file_uploader("Upload Your Resume 📄", accept_multiple_files=False, type=['pdf'])

# Process the uploaded PDF resume
if upload_resume is not None:
    bytes_data = upload_resume.getvalue()
    pdf_text = pdf_loader(bytes_data)
    st.success("The pdf was uploaded successfully!")
else:
    st.warning("Upload pdf to continue..")

# Provide a text area for the user to paste the job description
job_description = st.text_area("Paste the job description below:")

# Generate the cover letter when the user clicks the button
if st.button("Generate Cover Letter"):
    with st.spinner():
        cover_letter = cl_generator(pdf_text, job_description, openai_key, temp)
    with st.expander("Cover Letter", expanded=True):
        st.code(cover_letter)
