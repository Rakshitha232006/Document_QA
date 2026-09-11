# Document Q&A

An AI-powered Document Question & Answer application built with Python, Streamlit, and Hugging Face Transformers.

The application allows users to upload a document and ask questions based on its content. The system extracts the text from the uploaded document and uses a Question Answering model to find the relevant answer.

## 🚀 Live Application

[Click here to use the Document Q&A application](https://documentapp-hkjo7dfx43rprqjykv5shq.streamlit.app/)

## 📌 Features

- 📄 Upload TXT files
- 📕 Upload PDF files
- 📝 Upload Word (.docx) files
- ❓ Ask questions about the uploaded document
- 🤖 AI-powered question answering
- ⚡ Simple and easy-to-use Streamlit interface
- ☁️ Deployed as a live web application using Streamlit

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- PyPDF2
- python-docx
- RoBERTa

## 🤖 AI Model

This project uses the Hugging Face Question Answering model:

deepset/roberta-base-squad2

The model is used to extract answers from the context provided by the uploaded document.

## 📂 Project Structure

Document_QA/
│
├── main.py
├── document_qna.py
├── requirements.txt
├── .gitignore
└── README.md

## ⚙️ How It Works

Upload Document
       ↓
Extract Text
       ↓
Enter Question
       ↓
Question Answering Model
       ↓
Generate Answer
       ↓
Display Answer

## 💻 Run Locally

### 1. Clone the repository

git clone https://github.com/Rakshitha232006/Document_QA.git

### 2. Open the project folder

cd Document_QA

### 3. Create a virtual environment

python -m venv .venv

### 4. Activate the virtual environment

Windows:

.venv\Scripts\activate

### 5. Install the required packages

pip install -r requirements.txt

### 6. Run the Streamlit application

streamlit run main.py

The application will open in your browser.

## 📄 Supported File Types

| File Type | Extension |
|-----------|-----------|
| Text | .txt |
| PDF | .pdf |
| Microsoft Word | .docx |

## 🧪 Example

Upload a document containing a story and ask:

Who was Arun?

The application analyzes the document and returns the answer based on its contents.

## 🌐 Deployment

The application is deployed using Streamlit and is available online:

[Open Document Q&A](https://documentapp-hkjo7dfx43rprqjykv5shq.streamlit.app/)

## 👩‍💻 Author

Rakshitha

GitHub: [Rakshitha232006](https://github.com/Rakshitha232006)

## 📜 License

This project is created for educational and project purposes.
