# Bucle que recorre todos los números enteros desde el 100 hasta el 300 (el 301 es el límite exclusivo)
for i in range(100, 301):
    
    # Evaluamos si el residuo de dividir el número actual entre 12 es diferente de cero.
    # El símbolo '%' calcula el residuo de una división entera.
    if (i % 12) != 0:
        
        # Si NO es divisible por 12, la instrucción 'continue' salta el resto del código
        # y pasa inmediatamente a la siguiente iteración (al siguiente número del bucle).
        continue
        
    # Si el número SÍ pasó la prueba anterior (es decir, es múltiplo exacto de 12), 
    # se imprime en la pantalla.
    print(i)
