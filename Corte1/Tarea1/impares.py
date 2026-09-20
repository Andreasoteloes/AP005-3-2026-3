# Ejemplos de Bucle para pares e impares ---
# for i in range (1,21):
#      residual = i%2
#      if residual == 0:
#          print(f'{i} is even')
#      else:
#          #print(f'{i} is odd')
#          print(str(i) + ' is odd')

#  Cálculo de cubos ---
# for i in range (0,6):
#      result = i**3
#      print(result)

# Programa principal activo ---

# 1. Solicitamos un valor al usuario mediante la consola. 
# La función 'input' guarda siempre la respuesta como un texto (string).
times = input("Enter a number of times: ")

# 2. Convertimos ese texto ingresado a un número decimal por seguridad (float).
times = float(times)

# 3. Convertimos inmediatamente ese número decimal a un número entero (int).
# Esto evita errores si el usuario llega a escribir un número con punto decimal (ej. "5.9" pasa a ser 5).
times = int(times)

# 4. Imprimimos en pantalla el tipo de dato final de la variable (veremos que es <class 'int'>).
print(type(times))

# 5. Imprimimos el valor numérico limpio que digitó el usuario.
print(times)

# 6. Evaluamos una condición para controlar el flujo del programa:
if times == 0:
    # Si el usuario ingresó 0, el programa no hace bucles e imprime este mensaje.
    print("Don't do anything")
else:
    # Si el número es diferente de 0 (ej. positivo), creamos un bucle 'for' 
    # que se repetirá desde el 1 hasta el número exacto que indicó el usuario ('times + 1').
    for i in range(1, times + 1):
        # En cada vuelta del bucle, imprimimos el valor actual de la variable 'i'.
        print("i = ", i)
