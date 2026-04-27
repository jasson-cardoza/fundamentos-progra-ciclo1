# 9. Juego de adivinar número
# Genera un número secreto.
# Con while, permite intentos hasta acertar.
# Usa if para dar pistas (mayor o menor).
# Luego usa for para mostrar todos los intentos realizados.

import random

secreto = random.randint(1, 100)
intentos = []

while True:
    numero = int(input("Adivina el número: "))
    intentos.append(numero)
    
    if numero == secreto:
        print("Correcto")
        break
    elif numero < secreto:
        print("Mayor")
    else:
        print("Menor")

print("Intentos realizados:")
for intento in intentos:
    print(intento)
