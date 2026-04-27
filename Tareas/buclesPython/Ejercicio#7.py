# 7. Promedio de notas
# Con while, permite ingresar notas hasta que el usuario escriba -1.
# Usa if para ignorar notas inválidas (menores a 0 o mayores a 10).
# Luego usa for para recorrer las notas válidas y calcular el promedio.

notas = []

while True:
    numero = float(input("Ingrese una nota (-1 para terminar): "))
    
    if numero == -1:
        break
    
    if numero >= 0 and numero <= 10:
        notas.append(numero)

suma = 0
for nota in notas:
    suma += nota

if len(notas) > 0:
    promedio = suma / len(notas)
    print("Promedio:", promedio)
else:
    print("No hay notas válidas")