# Ejercicio 4:
# Crear una función que reciba una lista de palabras y un número.
# La función debe transformar cada palabra de la lista según la opción seleccionada (1, 2 o 3).

def transformar_lista(lista_palabras, opcion):
    lista_transformada = []

    for palabra in lista_palabras:
        if opcion == 1:
            lista_transformada.append(palabra.upper())
        elif opcion == 2:
            lista_transformada.append(palabra.lower())
        elif opcion == 3:
            lista_transformada.append(palabra.capitalize())
        else:
            lista_transformada.append("Opción no válida")

    return lista_transformada


palabras = ["ogros", "cebollas", "pantano", "burro"]

# Prueba
resultado = transformar_lista(palabras, 3)
print(resultado)