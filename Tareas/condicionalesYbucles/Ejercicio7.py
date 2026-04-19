# Ejercicio 7:
# Solicita el monto de una compra y aplica:
# Más de 100: 20% de descuento
# Entre 50 y 100: 10% de descuento
# Menos de 50: sin descuento

monto = float(input("Ingresa el monto de la compra: "))

if monto > 100:
    total = monto * 0.8
elif 50 <= monto <= 100:
    total = monto * 0.9
else:
    total = monto

print("Total a pagar:", total)