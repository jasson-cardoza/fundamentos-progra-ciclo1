# Ejercicio 4
# Un script debe auditar una secuencia de 50 registros, pero debe ignorar registros corruptos y detenerse si detecta una amenaza de seguridad. Crea un bucle que recorra un rango de 1 a 50.

for i in range(1, 51):
    if i % 3 == 0:
        continue
    
    if i >= 42:
        break;
    
    print(f"Procesando registro ID: {i}")