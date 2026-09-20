# 1. Importamos la librería 'time' para poder usar funciones de pausa y tiempo en el programa.
import time

# 2. Creamos una variable llamada 'cadena' que almacena la palabra de texto 'Python'.
cadena = 'Python'

# 3. Creamos un bucle 'for' para recorrer cada letra de la palabra, una por una.
for letra in cadena:
    
    # 4. Evaluamos una condición: si la letra actual que estamos revisando es exactamente 't':
    if letra == 't':
        # La instrucción 'continue' interrumpe la vuelta actual del bucle, 
        # saltándose todo lo que esté debajo, y pasa inmediatamente a la siguiente letra.
        continue
        
    # 5. Si la letra NO es 't', el programa continúa y la imprime en la pantalla.
    print(letra)
    
    # 6. Usamos 'time.sleep(1)' para hacer una pausa de exactamente 1 segundo 
    # antes de pasar a imprimir la siguiente letra.
    time.sleep(1)
