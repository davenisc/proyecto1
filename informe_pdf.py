from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


nombre_archivo = 'informe.pdf'

c = canvas.Canvas(nombre_archivo, pagesize=letter)

c.setFont("Helvetica", 12)

x = 100
y = 750

texto = "Este es un informe PDF generado desde python"

c.drawString(x, y, texto)

c.save()

print(f"El informe PDF {nombre_archivo} se genero con exito!")

