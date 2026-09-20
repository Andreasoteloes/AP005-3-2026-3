# ==========================================
# 9) Imprimir números primos entre 0 y 30
# ==========================================

# Definimos el límite superior del rango hasta donde queremos buscar (menor a 30).
tope_rango = 30
n = 0
primo = True

# Bucle 'while' que recorre los números desde el 0 hasta el 29.
while (n < tope_rango):
    
    # Bucle 'for' que prueba dividir 'n' entre todos los números desde el 2 hasta antes de llegar a 'n'.
    for div in range(2, n):
        # Si el residuo de la división es 0, significa que encontró un divisor exacto.
        if (n % div == 0):
            primo = False # El número ya no es primo.
            
    # Si la bandera 'primo' sigue siendo True, significa que es un número primo y se imprime.
    if (primo):
        print(n)
    else:
        # Si no era primo, restablecemos la bandera a True para el siguiente número.
        primo = True
        
    # Incrementamos el valor de 'n' en 1 para pasar al siguiente número.
    n += 1


# ==========================================
# 10) Optimización del punto 9 usando 'break'
# ==========================================

n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            
            # OPTIMIZACIÓN: Si encontramos que el número NO es primo, 
            # no tiene sentido seguir probando con los demás divisores. 
            # Usamos 'break' para romper el bucle 'for' inmediatamente y ahorrar ciclos.
            break
            
    if (primo):
        print(n)
    else:
        primo = True
    n += 1


# ==========================================
# 11) Medición de la optimización (Hasta 30)
# ==========================================

# --- Evaluando código SIN break ---
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1 # Contamos cuántas veces se ejecuta el bucle interno.
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))


# --- Evaluando código CON break ---
ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1 # Contamos los ciclos en la versión optimizada.
        if (n % div == 0):
            primo = False
            break # Rompe el ciclo anticipadamente.
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))

# Calculamos y mostramos el porcentaje de reducción de ciclos que logró el 'break'.
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')


# ==========================================
# 12) Comprobando si la optimización crece al aumentar el rango (A 100)
# ==========================================

# Ampliamos el rango de búsqueda a 100 para evaluar el rendimiento a mayor escala.
tope_rango = 100

# --- Prueba SIN break con rango 100 ---
ciclos_sin_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_sin_break += 1
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))

# --- Prueba CON break con rango 100 ---
ciclos_con_break = 0
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        ciclos_con_break += 1
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))

# Mostramos el nuevo porcentaje comparativo de ciclos con un rango mayor.
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')
