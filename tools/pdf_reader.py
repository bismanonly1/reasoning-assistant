import pypdf

def read_pdf(file_path):
    pdf_reader = pypdf.PdfReader(file_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text