# 4. Suma de números impares
# Con while, pide números hasta que se ingrese 0.
# Usa if para sumar solo los números impares.
# Luego usa for para imprimir cada número impar ingresado.

suma = 0
impares = []

while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    if numero % 2 != 0:
        suma += numero
        impares.append(numero)

print("Suma de impares:", suma)

for num in impares:
    print(num)