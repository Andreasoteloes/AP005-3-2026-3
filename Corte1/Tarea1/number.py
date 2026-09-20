# 1. Importamos la librería 'random' para poder generar números aleatorios.
import random

# 2. Importamos el módulo 'pyplot' de la librería 'matplotlib' y le asignamos el alias 'plt'.
# Esta herramienta nos permite dibujar gráficos y visualizaciones de datos.
from matplotlib import pyplot as plt

# --- Datos para el gráfico ---

# 3. Creamos una secuencia de números del 1 al 12 (el 13 es exclusivo). 
# Estos valores se utilizarán para la coordenada X (eje horizontal).
numbers_a = range(1, 13)

# 4. Generamos una lista de 12 números aleatorios enteros entre el 1 y el 1000 
# utilizando una comprensión de listas y la función 'randint'. 
# Estos valores se utilizarán para la coordenada Y (eje vertical).
numbers_b = [random.randint(1, 1000) for i in range(12)]

# --- Creación y visualización del gráfico ---

# 5. Indicamos a la librería que dibuje un gráfico de líneas 
# cruzando los valores de la X (numbers_a) con los valores de la Y (numbers_b).
plt.plot(numbers_a, numbers_b)

# 6. Mostramos el gráfico final en pantalla para que el usuario pueda visualizarlo.
plt.show()
