 ## Ejercicio 1:
    ## Crear una función que reciba un texto y un número. Según el número:
    ## 1. Convertir todo el texto a mayúsculas
    ## 2. Convertir todo el texto a minúsculas
    ## 3. Colocar la primera letra en mayúscula

def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción no válida"


# Frases del buen sherk
frase1 = "los ogros son como las cebollas"
frase2 = "esta es la parte en la que sales corriendo"
frase3 = "mejor afuera que adentro siempre digo"

# Pruebas
print(transformar_texto(frase1, 1))  # MAYÚSCULAS
print(transformar_texto(frase2, 2))  # minúsculas
print(transformar_texto(frase3, 3))  # Primera letra en mayúscula