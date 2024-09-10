import matplotlib.pyplot as plt

# Datos para la gráfica
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear la gráfica
plt.figure(figsize=(10, 6))  # Tamaño de la figura
plt.plot(x, y, marker='o', linestyle='-', color='b')  # Gráfica de líneas con puntos marcados
plt.title('Gráfica de Ejemplo')  # Título de la gráfica
plt.xlabel('Eje X')  # Etiqueta del eje X
plt.ylabel('Eje Y')  # Etiqueta del eje Y
plt.grid(True)  # Mostrar la cuadrícula
plt.show()  # Mostrar la gráfica
