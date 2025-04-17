import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame simple
data = {'Mes': ['Enero', 'Febrero', 'Marzo'], 'Ventas': [100, 150, 200]}
df = pd.DataFrame(data)

# Mostrar por consola
print(df)

# Graficar
plt.plot(df['Mes'], df['Ventas'], marker='o')
plt.title('Ventas por mes')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.grid(True)
plt.savefig('grafico.png')  # Guarda la imagen
plt.show()
