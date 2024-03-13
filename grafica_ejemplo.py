import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('D:\curso_python_virtual\Febrero\modulo7\datos.csv')

df['Fecha'] = pd.to_datetime(df['Fecha'])

plt.plot(df['Fecha'], df['Valor'], marker='o', linestyle='-', color='b')

plt.title('Evolucion de los valores')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.grid(True)


plt.show()
