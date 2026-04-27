# 10. Suma acumulativa con límite
# Con while, pide números hasta que la suma supere 100.
# Usa if para ignorar números negativos.
# Luego usa for para mostrar todos los números válidos ingresados.

suma = 0
numeros = []

while suma <= 100:
    numero = int(input("Ingrese un número: "))
    
    if numero >= 0:
        suma += numero
        numeros.append(numero)

print("Números válidos ingresados:")
for n in numeros:
    print(n)