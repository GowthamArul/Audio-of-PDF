from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hi, This program is for reading the PDF file using python pyttsx3 Library')
pdf.output('Tuto.pdf', 'F')
