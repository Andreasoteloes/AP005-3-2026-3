# 1. Inicializamos la variable 'a' con el valor 1 para permitir que el bucle 'while' arranque por primera vez.
a = 1

# 2. Solicitamos un número al usuario mediante la consola y lo guardamos como texto.
value = input('Ingrese un valor')

# 3. Convertimos ese texto ingresado a un número entero (int) para poder usarlo en operaciones matemáticas.
value = int(value)

# 4. Creamos un bucle principal ('while') que se repetirá indefinidamente 
# siempre y cuando la variable 'a' mantenga el valor de 1.
while a == 1:
    
    # 5. Creamos un bucle 'for' que recorre los números desde el 1 hasta el número ingresado ('value + 1').
    for i in range(1, value + 1):
        
        # Para cada número que recorremos, reiniciamos el contador de divisores en 0.
        conta = 0
        
        # 6. Creamos un bucle secundario (anidado) que va desde el 1 hasta el número actual ('i + 1').
        for n in range(1, i + 1):
            
            # Calculamos el residuo de dividir 'i' entre 'n' usando el operador módulo ('%').
            residue = i % n
            
            # Si el residuo es 0, significa que 'n' divide exactamente a 'i'.
            if residue == 0:
                conta = conta + 1
                  
            # Nota: Las siguientes líneas están comentadas; sirven para depurar 
            # y ver paso a paso cómo cambian las variables si se descomentan.
            # print("i = ", i)
            # print("n = ", n)
            # print("residue = ", residue)
            # print("conta = ", conta)
            
    # 7. Una vez que el bucle 'for' termina de revisar todos los números hasta el límite, 
    # evaluamos si el último número analizado tiene exactamente 2 divisores (propiedad de los primos).
    if conta == 2:
       print(f'{i} es un primo')
       print("\n") # Imprime un salto de línea adicional para ordenar la consola.
    else:
       print(f'{i} NOOO es un primo')
       print("\n")

    # 8. Preguntamos al usuario si desea repetir el proceso.
    print('Do you want to continue?. Press 1 to do that')
    
    # Capturamos la respuesta del usuario y la convertimos a número entero.
    a = input()
    a = int(a)

    # 9. Si el usuario escribe cualquier número diferente de 1, se rompe el bucle y termina el programa.
    if a != 1:
        break

    # 10. Si el usuario decide continuar (escribió 1), le pedimos un nuevo valor para repetir el ciclo.
    value = input('Ingrese un valor')
    value = int(value)
