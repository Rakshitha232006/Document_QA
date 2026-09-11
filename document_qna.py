from transformers import pipeline
from PyPDF2 import PdfReader
from docx import Document


# Load the model
question_answer = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2"
)


# Read TXT file
def read_txt(file):
    return file.read().decode("utf-8")


# Read PDF file
def read_pdf(file):
    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# Read Word file
def read_docx(file):
    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


# Read uploaded file
def read_file_content(file):

    if file.name.lower().endswith(".txt"):
        return read_txt(file)

    elif file.name.lower().endswith(".pdf"):
        return read_pdf(file)

    elif file.name.lower().endswith(".docx"):
        return read_docx(file)

    else:
        return ""


# Get answer
def get_answer(file, question):

    context = read_file_content(file)

    if not context.strip():
        return "Could not extract text from the uploaded file."

    answer = question_answer(
        question=question,
        context=context
    )

    return answer["answer"]