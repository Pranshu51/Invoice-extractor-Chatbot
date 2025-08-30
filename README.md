🧾 Invoice-Extractor-Chatbot
This project is an intelligent chatbot designed to extract key information from invoices and answer user queries based on the extracted data. Leveraging the power of Large Language Models (LLMs) and a Streamlit user interface, this application provides a simple and efficient way to interact with your financial documents.

✨ Features
Invoice Processing: Automatically reads and processes PDF invoices.

Intelligent Chat: Answers questions about invoice details (e.g., total amount, vendor, date) using a conversational interface.

Context-Aware Responses: Utilizes a Retrieval Augmented Generation (RAG) system to ensure answers are grounded in the content of the provided invoices.

Simple UI: A user-friendly interface built with Streamlit for easy uploading and interaction.

💻 Technologies Used
Python: The core programming language for the backend logic.

Streamlit: For creating the interactive web application interface.

Google Gemini API: The powerful LLM that drives the conversational AI.

LangChain: Framework for building the RAG pipeline.

PyPDF2: For extracting text from PDF documents.

FAISS: For efficient similarity search and vector storage.

🚀 Installation & Setup
Clone the repository:

git clone [https://github.com/Pranshu51/Invoice-extractor-Chatbot.git](https://github.com/Pranshu51/Invoice-extractor-Chatbot.git)
cd Invoice-extractor-Chatbot

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

Windows:

.\venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

(Note: You will need to create a requirements.txt file from your project's dependencies, e.g., pip freeze > requirements.txt).

Set up your Google API Key:

Create a .env file in the root directory of your project.

Add your Google API key to the file in the following format:

GOOGLE_API_KEY="your_api_key_here"

▶️ Usage
Run the Streamlit app:

streamlit run app.py

Your browser will open automatically, displaying the application.

Upload your PDF invoices and click "Process."

Type your questions into the chat box to get started!
