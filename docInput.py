import docx
import PyPDF2
import textract
from pathlib import Path


def extract_text_from_file(file_path):
    file_extension = Path(file_path).suffix.lower()
    text=""

    if file_extension == ".doc"  :
        # Extract text from DOCX file
        doc = docx.Document(file_path)

        for paragraph in doc.paragraphs:
          text += paragraph.text + "\n"  # Add a newline after each paragraph

    elif file_extension == ".pdf":
        # Extract text from PDF file
        with open(file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        # Remove "Powered by TCPDF" footer
        text = text.replace("Powered by TCPDF (www.tcpdf.org)", "")

    elif file_extension == ".txt":
        # Extract text from TXT file
        with open(file_path, "r", encoding="utf-8") as txt_file:
            text = txt_file.read()

    else:
        raise ValueError("Unsupported file format. Only DOCX, PDF, and TXT are supported.")

    return text