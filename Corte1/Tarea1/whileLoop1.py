# Bucle principal 'for' que teóricamente recorrerá los números desde el 1 hasta el 5 (el 6 es exclusivo).
for i in range(1, 6):
    
    # Bucle 'while' anidado que se repetirá siempre y cuando la variable 'i' sea menor o igual a 4.
    while i <= 4:
        # Incrementamos el valor de 'i' sumándole 1 en cada vuelta del while.
        i += 1
        # Imprimimos en la consola el valor actual que tiene 'i'.
        print(i)
        
    # IMPORTANTE: Este 'break' está dentro del bucle 'for', justo al salir del 'while'.
    # En cuanto el bucle 'while' termina de cumplirse, se ejecuta esta orden 
    # que rompe y detiene por completo el bucle principal 'for' en su primera y única vuelta.
    break
