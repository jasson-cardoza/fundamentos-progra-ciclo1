# 8. Patrón de asteriscos
# Pide un número.
# Usa for para imprimir un triángulo de asteriscos.
# Usa if para que solo imprima filas impares.
# Repite con while hasta que el usuario ingrese 0.

while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    
    if numero == 0:
        break

    print("Usando for:")
    for i in range(1, numero + 1):
        if i % 2 != 0:
            print("*" * i)

    print("Usando while:")
    i = 1
    while i <= numero:
        if i % 2 != 0:
            print("*" * i)
        i += 1