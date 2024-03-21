import matplotlib.pyplot as plt

# Datos para el gráfico de pastel
asignaturas = ['Matemáticas', 'Ciencias', 'Literatura', 'Inglés']
promedios = [90, 88, 78, 93]

# Colores para el gráfico
colores = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Crear el gráfico de pastel
plt.figure(figsize=(8, 6))
plt.pie(promedios, labels=asignaturas, autopct='%1.1f%%', colors=colores, startangle=140)
plt.title('Promedio de Asignaturas')
plt.axis('equal')

# Guardar el gráfico como una imagen
plt.savefig('grafico_pastel.png')
