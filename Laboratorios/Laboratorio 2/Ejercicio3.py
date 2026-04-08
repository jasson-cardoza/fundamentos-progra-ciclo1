# Ejercicio 3:
# Solicitar al usuario un texto y un número. Enviar esos datos a una función
# que aplique la transformación según la opción elegida.

def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción no válida"


# Pedir el texto (pd: me gustan las peliculas del sherk xD)
texto = input("Ingresa una frase (ej: los ogros son como las cebollas): ")
opcion = int(input("Elige una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Capitalizar): "))

# Llamar a la función y imprimir el resultado
resultado = transformar_texto(texto, opcion)
print("Resultado:", resultado)