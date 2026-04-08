# Ejercicio:
# Crear una función que reciba un texto y un número, transforme el texto según la opción
# y luego devuelva la cantidad de caracteres del resultado.

def transformar_y_contar(texto, opcion):
    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        resultado = texto.capitalize()
    else:
        return "Opción inválida"
    
    return len(resultado)


# Pruebas
print(transformar_y_contar("los ogros son como las cebollas", 1))
print(transformar_y_contar("los ogros son como las cebollas", 3))