resume_parser.py
import PyPDF2
import docx


def extract_text_from_pdf(file):
pdf_reader = PyPDF2.PdfReader(file)
text = ""
for page in pdf_reader.pages:
text += page.extract_text()
return text


def extract_text_from_docx(file):
doc = docx.Document(file)
return " ".join([para.text for para in doc.paragraphs])


#Add this in app.py#
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))


def clean_text(text):
text = re.sub(r'[^a-zA-Z]', ' ', text)
text = text.lower()
words = text.split()
words = [w for w in words if w not in stop_words]
return ' '.join(words)
