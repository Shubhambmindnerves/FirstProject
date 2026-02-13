from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def create_pdf(summary_text):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    elements = []

    styles = getSampleStyleSheet()
    style = styles["Normal"]

    for line in summary_text.split("\n"):
        elements.append(Paragraph(line, style))
        elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)
    buffer.seek(0)

    return buffer
