#Ejercicio 3
#  Un sensor industrial envía lecturas de temperatura. Debes programar la lógica que decida qué alertas disparar según los valores recibidos.

temperaturas = []

for i in range(5):
    temp = int(input("Ingrese una temperatura: "))
    temperaturas.append(temp)

for temp in temperaturas:
    match temp:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            print("Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico")