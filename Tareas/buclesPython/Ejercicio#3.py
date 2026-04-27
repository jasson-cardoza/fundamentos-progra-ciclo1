# 3. Tabla de multiplicar filtrada
# Pide un número.
# Con for, genera su tabla del 1 al 10.
# Usa if para mostrar solo resultados mayores a 20.
# Repite con while hasta que el usuario escriba -1.

while True:
    numero = int(input("Ingrese un número (-1 para salir): "))
    
    if numero == -1:
        break

    print("Usando for:")
    for i in range(1, 11):
        resultado = numero * i
        if resultado > 20:
            print(numero, "x", i, "=", resultado)

    print("Usando while:")
    i = 1
    while i <= 10:
        resultado = numero * i
        if resultado > 20:
            print(numero, "x", i, "=", resultado)
        i += 1