# 📄 PDF Query Application

![Screenshot (237)](https://github.com/user-attachments/assets/0bc24d0c-a334-44e9-8679-8743f778ba4f)

This Streamlit application allows users to upload a PDF document and ask questions about its content using an AI model. The application utilizes the Groq API and the LLaMA model from Hugging Face to 
provide answers based on the extracted text from the PDF.

## 🚀 Features

- **PDF Upload**: Easily upload any PDF document.
- **Text Extraction**: Extract text from the uploaded PDF.
- **Question Answering**: Ask questions about the PDF content and get accurate answers.
- **User-Friendly UI**: Enhanced with Streamlit's components, sidebars, buttons, icons, and color contrasts.

## 🛠️ Installation

To run this application locally, follow the steps below.

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Groq API key

### Step-by-Step Guide

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/pdf-query-app.git
   cd pdf-query-app
   ```

2. **Install the Required Packages**:

   Install all the required Python libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Get Groq API Key**:

   - Sign up or log in to [Groq](https://www.groq.com).
   - Obtain your API key by navigating to your account settings and selecting API keys.
   - Set your API key in the environment variables by running:

   ```bash
   export GROQ_API_KEY=<your-api-key-here>
   ```

4. **Run the Application**:

   Start the Streamlit app by running:

   ```bash
   streamlit run app.py
   ```

   Open the provided URL in your web browser to use the app.

## 🧑‍💻 Using the App

1. **Upload a PDF**: Click the "Upload a PDF file" button and select a PDF from your device.
2. **Extract Text**: Once the PDF is uploaded, the text will be extracted and displayed in the text area.
3. **Ask a Question**: Enter your query about the PDF content in the input box.
4. **Get Answer**: Click the "Get Answer" button to generate a response based on your query.

## 🤖 Models Used

### LLaMA-2 Model from Hugging Face

- **Model Name**: `meta-llama/Llama-2-7b-hf`
- **Description**: This model is optimized for natural language understanding and question-answering tasks.
- **Link to Model**: [LLaMA-2 on Hugging Face](https://huggingface.co/meta-llama/Llama-2-7b-hf)

To use this model in your app:

```python
from transformers import AutoTokenizer, LlamaForCausalLM

model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
```

### Access and Use LLaMA-2 on Hugging Face

To access this model:
1. Visit the [LLaMA-2 Model page on Hugging Face](https://huggingface.co/meta-llama/Llama-2-7b-hf).
2. If it's a gated model, request access and ensure you are logged into your Hugging Face account.

## 🧰 Requirements

Below are the packages required for this application:

```plaintext
streamlit
groq
pdfplumber
torch
transformers
```

## 🖼️ Demo

Try the demo of this app on Hugging Face Spaces to see it in action!

- **Link to Hugging Face Space**: [Demo on Hugging Face](https://huggingface.co/spaces/mohAhmad/RAGMODEL)

## 📃 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙌 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 🌟 Acknowledgments

- [Streamlit](https://streamlit.io) for providing an easy-to-use web application framework.
- [Groq](https://www.groq.com) for their powerful API for language models.
- [Hugging Face](https://huggingface.co) for hosting models and providing access to state-of-the-art NLP models.


Made with ❤️ by [Ahmad Raza](https://www.linkedin.com/in/ahmadkhushi).
