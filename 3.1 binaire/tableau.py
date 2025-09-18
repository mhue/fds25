from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors

# Paths - using your PNG files
human_img_path = "3.1 binaire/human.png"
alien_img_path = "3.1 binaire/alien_white_bg_clean.png"
pdf_path = "3.1 binaire/tableau_bibi.pdf"

# Document portrait A4
doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=15*mm, rightMargin=15*mm, topMargin=15*mm, bottomMargin=15*mm)
elements = []

# Images with preserved aspect ratio, constrained to column width
human_img = Image(human_img_path, width=85*mm, height=80*mm)
alien_img = Image(alien_img_path, width=85*mm, height=80*mm)

# Table data with images row and headers
data = [
    [human_img, alien_img],
    ["Humain", "Bibi"],
]

# Add rows 0–8 with trimmed binary (no leading zeros, except keep "0")
for i in range(9):
    bin_str = bin(i)[2:]
    data.append([str(i), bin_str])

# Table with equal column widths
table = Table(data, colWidths=[85*mm, 85*mm], hAlign="CENTER")

# Style
table.setStyle(TableStyle([
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("ALIGN", (1, 1), (1, -1), "RIGHT"),   # right-align "Bibi" and binary numbers
    ("VALIGN", (0, 0), (1, 1), "MIDDLE"),
    ("VALIGN", (0, 2), (1, -1), "BOTTOM"), 
    ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 24),
    ("TOPPADDING", (0, 0), (-1, -1), 18),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
    ("TOPPADDING", (0, 1), (-1, 1), 0),
    ("BOTTOMPADDING", (0, 1), (-1, 1), 20),
    ("RIGHTPADDING", (1, 1), (1, -1), 100),   # right padding for "Bibi" and binary numbers alignment
    ("LINEAFTER", (0, 0), (0, -1), 1.5, colors.black),
    ("BACKGROUND", (0, 1), (-1, 1), colors.whitesmoke),
]))

# Adjust row height for image row
table._argH[0] = 85*mm

elements.append(table)

# Build PDF
doc.build(elements)
