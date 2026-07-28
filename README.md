# ai-research-assistant
AI Research Assistant is a full-stack Python application built with FastAPI, TensorFlow, and Streamlit. It automates PDF document processing, local text extraction, and content classification, providing a seamless dashboard for managing and analyzing research papers efficiently.
AI Research Assistant
AI Research Assistant is a full-stack Python application built with FastAPI, TensorFlow, and Streamlit. It automates PDF document processing, local text extraction, and content classification, providing a seamless dashboard for managing and analyzing research papers efficiently.

Features
FastAPI Backend: High-performance asynchronous API endpoints for handling document uploads and processing pipelines.

TensorFlow Classifier: Local deep learning model integration for automated document content classification.

Streamlit Dashboard: Interactive user interface for uploading research papers, viewing extraction metrics, and interacting with the system.

Local Processing: Extracts text, chunks documents, and runs predictions completely offline without depending on external cloud services for core processing.

Tech Stack
Backend: Python, FastAPI, Uvicorn

Machine Learning: TensorFlow, Keras

Frontend: Streamlit

Document Processing: pypdf / pdfplumber

Project Structure
Plaintext
ai-research-assistant/
│
├── frontend/
│   └── app.py              # Streamlit user interface dashboard
│
├── main.py                 # FastAPI backend server and routes
├── requirements.txt        # Project dependencies
├── .gitignore              # Ignored files (venv, cache, etc.)
└── LICENSE                 # MIT License
Getting Started
1. Clone the Repository
DOS
git clone https://github.com/BokkaHemaLakshmi/ai-research-assistant.git
cd ai-research-assistant
2. Set Up a Virtual Environment
DOS
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
DOS
pip install -r requirements.txt
4. Run the Backend Server
DOS
uvicorn main:app --reload
5. Run the Frontend Dashboard
Open a separate terminal window, activate your virtual environment, and launch Streamlit:

DOS
venv\Scripts\activate
streamlit run frontend/app.py
License
This proj
