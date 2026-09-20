# 'while True' crea un bucle infinito. Esto significa que el programa se repetirá
# una y otra vez de forma continua hasta que cerremos el programa manualmente.
while True:

    # 1. Solicitamos un número al usuario mediante la consola.
    # La función 'input' lee lo que escribe el usuario y 'int()' lo convierte a un número entero.
    value = int(input("Enter a positive integer value: "))
    
    # 2. Imprimimos en pantalla el valor que acaba de digitar el usuario para confirmarlo.
    print("Value: ", value)
    
    # 3. Verificamos si la variable 'value' es de tipo entero (int).
    # La función 'isinstance' devuelve True si coincide con el tipo de dato o False si no.
    a = isinstance(value, int)
    
    # 4. Evaluamos una condición doble: que 'a' sea Verdadero Y que el número sea mayor a 0 (positivo).
    if a == True and value > 0:
        
        # Inicializamos una variable llamada 'fact' en 1. 
        # Esta variable servirá como una "caja" para acumular la multiplicación del factorial.
        fact = 1
        
        # 5. Creamos un bucle 'for' que va desde el número 1 hasta el número ingresado ('value').
        # Nota: 'range' detiene su conteo antes del número final, por eso ponemos 'value + 1'.
        for i in range (1, value + 1):
            
            # En cada paso del bucle, multiplicamos lo que ya teníamos en 'fact' 
            # por el número actual de la vuelta ('i').
            fact = fact * i            
        
        # 6. Una vez termina de multiplicarse todo, imprimimos el resultado final del factorial.
        print(f'The factorial of {value} is: ', fact)
        
    # 7. Si el número ingresado es menor o igual a 0, se activa esta parte alternativa (else).
    else:
        # Imprimimos un mensaje de advertencia pidiendo un número positivo.
        print("Please, enter a positive integer number")
