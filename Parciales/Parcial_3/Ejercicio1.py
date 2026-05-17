# Ejercicio 1
# Se trabaja para una empresa de envíos. Recibes códigos de rastreo con el formato AÑO-CATEGORÍA-PAÍS (ejemplo: 2024-TECNOLOGIA-ES). Tu tarea es automatizar la clasificación de estos paquetes siguiendo estas instrucciones:

etiqueta = input("Escriba la etiqueta de rastreo todo en mayuscula: ")

if etiqueta == "" or etiqueta is None:
    print("Error: entrada inválida")
else:
    categoria = etiqueta.split("-")[1]
    print(categoria)
    print("Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional")