import pathlib
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Frame, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import requests
import json

__OUT_DIR_NAME = "Jokes_PDF_JPEG"
__OUT_DIR = pathlib.Path(__file__).parent.joinpath(__OUT_DIR_NAME)

FILES_DIR = pathlib.Path(__file__).parent.joinpath("files")

PAGE_PADDING = 2 * cm

F1_H = 11 * cm
F1_W = 17 * cm
F1_Y = A4[1] - F1_H - PAGE_PADDING

def get_jokes():
    joke_url_single = requests.get(
        'https://v2.jokeapi.dev/joke/Programming')
    json_joke = json.loads(joke_url_single.text)
    if json_joke["type"] == "single":
        return(json_joke["joke"])
    else:
        return(f"{json_joke['setup']}\n{json_joke['delivery']}")

def draw_jokes(canvas):
    stylesheet = getSampleStyleSheet()
    f1 = Frame(PAGE_PADDING, F1_Y, F1_W, F1_H, showBoundary=1)

    s_t = Spacer(1 * cm, 0.5 * cm)
    s = Spacer(1*cm, 0.2*cm)

    t_style = stylesheet["Heading4"]
    t_style.alignment = 1
    t1 = Paragraph("10 Jokes", t_style)

    p_style = stylesheet["Normal"]
    p1 = Paragraph(f"1.{get_jokes()}", p_style)
    p2 = Paragraph(f"2.{get_jokes()}", p_style)
    p3 = Paragraph(f"3.{get_jokes()}", p_style)
    p4 = Paragraph(f"4.{get_jokes()}", p_style)
    p5 = Paragraph(f"5.{get_jokes()}", p_style)
    p6 = Paragraph(f"6.{get_jokes()}", p_style)
    p7 = Paragraph(f"7.{get_jokes()}", p_style)
    p8 = Paragraph(f"8.{get_jokes()}", p_style)
    p9 = Paragraph(f"9.{get_jokes()}", p_style)
    p10 = Paragraph(f"10.{get_jokes()}", p_style)


    f1.add(t1, canvas)
    f1.add(s_t, canvas)
    f1.add(p1, canvas)
    f1.add(s, canvas)
    f1.add(p2, canvas)
    f1.add(s, canvas)
    f1.add(p3, canvas)
    f1.add(s, canvas)
    f1.add(p4, canvas)
    f1.add(s, canvas)
    f1.add(p5, canvas)
    f1.add(s, canvas)
    f1.add(p6, canvas)
    f1.add(s, canvas)
    f1.add(p7, canvas)
    f1.add(s, canvas)
    f1.add(p8, canvas)
    f1.add(s, canvas)
    f1.add(p9, canvas)
    f1.add(s, canvas)
    f1.add(p10, canvas)

    f1.drawBoundary(canvas)


def generate():
    """Generate 10 jokes writen in a PDF."""
    __OUT_DIR.mkdir(exist_ok=True)
    canv = Canvas(str(__OUT_DIR.joinpath(f"jokes.pdf")), pagesize=A4)

    draw_jokes(canv)

    canv.showPage()
    canv.save()
