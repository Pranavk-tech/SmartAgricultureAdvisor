from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib import styles

def create_pdf(data,filename):

    doc=SimpleDocTemplate(filename)

    style=styles.getSampleStyleSheet()

    content=[]

    title=Paragraph(
        "Smart Agriculture Advisor Report",
        style["Title"]
    )

    content.append(title)

    content.append(
        Paragraph("<br/><br/>",style["Normal"])
    )

    for key,value in data.items():

        line=Paragraph(
        f"<b>{key}</b>: {value}",
        style["BodyText"]
        )

        content.append(line)

    doc.build(content)