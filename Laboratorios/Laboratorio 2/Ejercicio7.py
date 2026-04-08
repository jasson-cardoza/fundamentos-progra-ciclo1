# Ejercicio:
# Crear una función que reciba un texto y una lista de números (entre 1 y 3).
# La función debe aplicar cada transformación en orden y devolver el resultado final.

def transformar_multiple(texto, lista_opciones):
    resultado = texto

    for opcion in lista_opciones:
        if opcion == 1:
            resultado = resultado.upper()
        elif opcion == 2:
            resultado = resultado.lower()
        elif opcion == 3:
            resultado = resultado.capitalize()
        else:
            return "Opción inválida"

    return resultado


# Pruebas
print(transformar_multiple("los ogros son como las cebollas", [1, 3]))
print(transformar_multiple("LOS OGROS SON COMO LAS CEBOLLAS", [2, 3]))