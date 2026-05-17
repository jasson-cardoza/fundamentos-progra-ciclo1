from decimal import Decimal

total = Decimal("0")

while True:
    try:
        entrada = input("Ingrese el precio del producto (0 para salir): ")
        
        if entrada == "0":
            break
        
        precio = Decimal(entrada)
        total += precio

    except ValueError:
        print("Advertencia: debe ingresar un número válido.")

print(f"Total acumulado: {total}")