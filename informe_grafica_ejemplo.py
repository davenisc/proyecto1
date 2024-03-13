import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


df = pd.read_csv('D:\curso_python_virtual\Febrero\modulo7\datos.csv')

#configuracion de la grafica
plt.figure(figsize=(6, 4))
plt.plot(df['Fecha'], df['Valor'], marker='o', linestyle='-', color='b')
plt.title('Evolución de los Valores')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.xticks(rotation=45)
plt.tight_layout()

#guardar la grafica como imagen
nombre = "Dave"

plt.savefig('grafica.png')
plt.close()

nombre_archivo = ('informe_pdf_con_grafica.pdf')

c = canvas.Canvas(nombre_archivo, pagesize=letter)
c.setFont("Helvetica", 12)

texto = "Informe PDF con Gráfica"
c.drawString(100, 750, texto)

c.drawString(100, 760, nombre)

# Insertar la imagen de la gráfica en el PDF
c.drawImage('grafica.png', 100, 500, width=400, height=200)  # Ajusta las dimensiones según sea necesario

c.save()
print(f'Informe PDF "{nombre_archivo}" generado con éxito.')

