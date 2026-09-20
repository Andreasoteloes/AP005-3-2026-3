# 1. Solicitamos un valor al usuario mediante la consola. 
# La función 'input' siempre guarda lo que escribe el usuario como un texto (string).
a = input("Enter a number: ")

# 2. Convertimos ese texto guardado en 'a' a un número entero usando 'int()'.
a = int(a)

# 3. Solicitamos un segundo valor al usuario, que también entra inicialmente como texto.
b = input("Enter b number: ")

# 4. Convertimos ese texto guardado en 'b' a un número decimal (con punto flotante) usando 'float()'.
b = float(b)

# 5. Sumamos ambas variables. Como Python es inteligente, al sumar un entero (int) 
# y un decimal (float), el resultado 'c' se convierte automáticamente en un número decimal.
c = a + b

# 6. Comparamos si el valor numérico de 'a' es exactamente igual al valor de 'b'.
if a == b:
    print("equal") # Se ejecuta si ambos números valen lo mismo (ej. si a = 5 y b = 5.0)
else:
    print("Different") # Se ejecuta si los valores son diferentes.

# 7. Imprimimos en pantalla el tipo de dato actual que tiene la variable 'a' (será <class 'int'>).
print("Type of a is: ", type(a))

# 8. Imprimimos en pantalla el tipo de dato actual que tiene la variable 'b' (será <class 'float'>).
print("Type of b is: ", type(b))

# 9. Imprimimos el resultado de la suma guardado en la variable 'c'.
print("c = ", c)

# 10. Comparamos si el TIPO DE DATO de 'a' es exactamente igual al TIPO DE DATO de 'b'.
if type(a) == type(b):
    print("a and b are of the same type")
else:
    # Como 'a' es entero y 'b' es decimal, entrará aquí y dirá que son de tipos diferentes.
    print("a and b are of different type")
