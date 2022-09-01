from pdf2image import convert_from_path
from pdf_jokes_generator import generate
import os


def generate_jpeg():
    """Converts a PDF file to JPEG"""
    poppler_path = "E:\\Discord Bot\\poppler-22.04.0\\Library\\bin"

    pdf_path = "E:\Discord Bot\Python_Jokes_Bot\Jokes_PDF_JPEG\jokes.pdf"

    pdf_to_jpeg = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)

    saving_folder ="E:\Discord Bot\Python_Jokes_Bot\Jokes_PDF_JPEG"
    generate()
    for page in pdf_to_jpeg:
        img_name = "jokes.jpeg"
        page.save(os.path.join(saving_folder, img_name), "JPEG")



