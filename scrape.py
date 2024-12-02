from newspaper import Article
import google.generativeai as genai
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

genai.configure(api_key=api_key)
# 

model = genai.GenerativeModel("gemini-1.5-flash")


def get_job_description(url):   
    try:
        print(url)
        article = Article(url)
        article.download()
        article.parse() 
        job_description = article.text
      
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return job_description

def read_pdf_file(name):
    pdf_file_name = 'mikecv.pdf'
    if os.path.exists(pdf_file_name):
        # Open and read the PDF
        reader = PdfReader(pdf_file_name)
        pdf_text = ""
        for page in reader.pages:
            pdf_text += page.extract_text()
        return pdf_text
    else:
        print(f"The file {pdf_file_name} does not exist in the current working directory.")


def generate_cover_letter(job_description, pdf_text):
    prompt_template = f"""
    You are a professional resume and cover letter writer with expertise in tailoring job applications to specific roles. Your task is to generate a compelling and personalized cover letter that aligns with the job description and my professional experience. 

    Here is the information you need:

    1. **Job Description**:
    {job_description}

    2. **My CV Details**:
    {pdf_text}

    3. **Instructions**:
    - Write the letter in a professional and confident tone.
    - Structure the letter as follows:
    - **Introduction**: Express interest in the role and briefly mention why I am a strong fit.
    - **Body**: Highlight 2-3 key achievements, skills, or experiences that align with the job requirements, using quantifiable examples where applicable.
    - **Conclusion**: Reiterate my enthusiasm for the role, mention how I can contribute to the company's goals, and include a call to action for further discussion.
    - Tailor the content to emphasize how my experience and skills directly align with the company's needs.
    - Ensure the letter is concise and polished, suitable for professional submission.

    Generate the cover letter based on the above information.
    """
    response = model.generate_content(prompt_template)
    return response.text















