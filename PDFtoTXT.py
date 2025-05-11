import pdfplumber
from pdfminer.high_level import extract_text
from tqdm import tqdm

ruta_pdf = "World Athletics Scoring Tables of Athletics.pdf"

with pdfplumber.open(ruta_pdf) as pdf:
    for page in tqdm(pdf.pages, desc="Extrayendo páginas"):
        texto = page.extract_text()
        with open("tablas_extraidas/tables.txt", "a", encoding="utf-8") as f:
            f.write(texto)