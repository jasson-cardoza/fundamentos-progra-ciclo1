# 6. Números primos en rango
# Pide un número n.
# Usa for para recorrer del 1 a n.
# Dentro, usa otro for con if para verificar si cada número es primo.
# Repite con while hasta que el usuario ingrese 0.

while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    
    if numero == 0:
        break

    print("Números primos:")
    for i in range(1, numero + 1):
        if i > 1:
            es_primo = True
            for j in range(2, i):
                if i % j == 0:
                    es_primo = False
            if es_primo:
                print(i)
