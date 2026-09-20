# 1. Importamos la librería 'time' para poder medir el tiempo exacto que tarda el programa en ejecutarse.
import time

# 2. Guardamos el momento exacto de inicio registrando el tiempo actual.
inicio = time.time()

# 3. Creamos un bucle principal ('for') que recorre todos los números enteros desde el 0 hasta el 30 (el 31 es exclusivo).
for i in range(0, 31):
    
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
              
    # 5. Evaluamos la regla matemática de los números primos: 
    # Un número primo es aquel que tiene exactamente 2 divisores (el 1 y él mismo).
    if conta == 2:
        # Si el contador es igual a 2, imprimimos que el número es primo.
        print(f'{i} es un primo')
        
# 6. Una vez termina de revisar todos los números, guardamos el tiempo final.
fin = time.time()

# 7. Calculamos la diferencia entre el tiempo final y el inicial, 
# y lo multiplicamos por 1000 para convertir el resultado a milisegundos (ms).
print("t = ", (fin - inicio) * 1000)
