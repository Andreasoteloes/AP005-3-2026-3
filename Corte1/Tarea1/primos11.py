# 1. Importamos la librería 'time' para medir el tiempo exacto de ejecución del programa.
import time

# 2. Registramos el momento exacto en que empieza a correr el script.
inicio = time.time()

# 3. Creamos un bucle principal ('for') que recorre los números desde el 1 hasta el 30 (el 31 es exclusivo).
# Nota: Empezar en 1 es más seguro para evitar evaluar el cero.
for i in range(1, 31):
    
    # Por cada número que evaluamos, inicializamos un contador de divisores en 0.
    conta = 0
    
    # 4. Creamos un bucle secundario (anidado) que va desde el 1 hasta el número actual ('i + 1').
    for n in range(1, i + 1):
        
        # Calculamos el residuo de dividir el número 'i' entre 'n' usando el operador módulo ('%').
        residue = i % n
        
        # Si el residuo es 0, significa que 'n' divide exactamente a 'i' (es un divisor).
        if residue == 0:
            # Aumentamos en 1 el contador de divisores.
            conta = conta + 1
              
    # 5. Evaluamos si el número cumple la regla de los números primos (exactamente 2 divisores).
    if conta == 2:
        # Si es primo, imprimimos el mensaje correspondiente.
        print(f'{i} es un primo')
        
        # 6. Imprimimos un salto de línea adicional ('\n') para dejar un espacio 
        # en blanco visual entre cada número primo impreso en la consola.
        print("\n")
        
# 7. Registramos el tiempo final una vez que el bucle termina de revisar todos los números.
fin = time.time()

# 8. Calculamos la diferencia entre el tiempo final y el inicial, 
# y la multiplicamos por 1000 para expresar el resultado en milisegundos (ms).
print("t = ", (fin - inicio) * 1000)
