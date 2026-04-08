# Ejercicio:
# Crear una función que reciba un texto y un número.
# Si el número no es 1, 2 o 3, debe mostrar un mensaje de “opción inválida”.

def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


# Pruebas
print(transformar_texto("los ogros son como las cebollas", 1))
print(transformar_texto("los ogros son como las cebollas", 4))  # inválida