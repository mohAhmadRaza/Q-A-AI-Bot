import streamlit as st
from groq import Groq
import pdfplumber
import os
import gc
from dotenv import load_dotenv

load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_response_groq(context, query):
    """Generate response using Groq API."""
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    response = chat_completion.choices[0].message.content
    return response

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Set the page layout to wide for better UI space
st.set_page_config(page_title="PDF Query Application", layout="wide")

# Sidebar
st.sidebar.title("PDF Query Assistant")
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/PDF_file_icon.svg/1024px-PDF_file_icon.svg.png", use_column_width=True)  # Adding an image in the sidebar
st.sidebar.markdown("### Navigation")
st.sidebar.markdown("Use this app to upload a PDF and ask questions about its content.")
st.sidebar.markdown("")

# Main UI layout
st.title("📄 PDF Query Application")
st.markdown("""
<style>
    .main-content {background-color: #f0f2f6; padding: 20px; border-radius: 10px;}
    .stButton>button {background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px;}
    .stTextInput>div>div>input {background-color: #f0f2f6; color: black; border-radius: 5px;}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-content'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    st.success("PDF uploaded successfully! 📄")
    document_text = extract_text_from_pdf(uploaded_file)
    st.text_area("📜 Extracted Text", document_text, height=200)

    query = st.text_input("🔍 Enter your query")

    if st.button("💬 Get Answer"):
        if query:
            with st.spinner("Generating response..."):
                response = generate_response_groq(document_text, query)
                st.write("**Response:**")
                st.write(response)

            # Clear memory after generating response
            gc.collect()
        else:
            st.error("Please enter a query.")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.sidebar.markdown("### About")
st.sidebar.info("Developed with ❤️ using Streamlit and Groq API.")
st.sidebar.markdown("---")
st.sidebar.write("For more information, visit [Groq](https://www.groq.com) and [Streamlit](https://streamlit.io).")

# Customize the theme and color contrast
st.markdown("""
<style>
    .css-1aumxhk {background-color: #E8EAF6;}
    .stTextInput>div>div>input {border-color: #3f51b5;}
    .stTextArea>div>div>textarea {border-color: #3f51b5;}
    .stButton>button {background-color: #3f51b5; color: white; font-size: 16px;}
</style>
""", unsafe_allow_html=True)