from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import PyPDF2
import io

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize model
model = genai.GenerativeModel('gemini-2.5-flash-lite')


# Function to get response from Gemini
def get_gemini_response(input_text, image=None, prompt=None):
    try:
        contents = []
        if input_text:
            contents.append(input_text)
        if image:
            contents.append(image)
        if prompt:
            contents.append(prompt)

        response = model.generate_content(contents)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# Streamlit UI
st.set_page_config(page_title="MultiLanguage Invoice Extractor", page_icon="🧾", layout="wide")
st.header("🧾 MultiLanguage Invoice Extractor")

# User input prompt
input_text = st.text_input("Enter custom instruction (e.g., 'Extract invoice number and total amount'):", key="input")

# File uploader
uploaded_file = st.file_uploader("Upload an Invoice (Image or PDF)", type=["jpg", "jpeg", "png", "pdf"])

# Process uploaded file
if uploaded_file is not None:
    file_type = uploaded_file.type

    if "pdf" in file_type:  # Handle PDF invoices
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text_data = ""
        for page in pdf_reader.pages:
            text_data += page.extract_text() + "\n"

        st.subheader("📄 Extracted Text from PDF")
        st.text_area("PDF Content", text_data, height=200)

        if st.button("Extract Information from PDF"):
            with st.spinner("Processing with Gemini..."):
                result = get_gemini_response(text_data, prompt=input_text)
            st.subheader("🔍 Extracted Information")
            st.write(result)

    else:  # Handle Image invoices
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Invoice", use_column_width=True)

        if st.button("Extract Information from Image"):
            with st.spinner("Processing with Gemini..."):
                result = get_gemini_response("Extract key invoice details", image=image, prompt=input_text)
            st.subheader("🔍 Extracted Information")
            st.write(result)
