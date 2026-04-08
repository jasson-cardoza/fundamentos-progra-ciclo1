# Ejercicio 2:
# Crear una función que reciba una palabra y un número, y muestre el resultado
# en pantalla aplicando la transformación correspondiente (1, 2 o 3).

def transformar_palabra(palabra, opcion):
    if opcion == 1:
        resultado = palabra.upper()
    elif opcion == 2:
        resultado = palabra.lower()
    elif opcion == 3:
        resultado = palabra.capitalize()
    else:
        resultado = "Opción no válida"
    
    print(resultado)

transformar_palabra("ogros", 1)       # MAYÚSCULAS
transformar_palabra("CEBOLLAS", 2)    # minúsculas
transformar_palabra("pantano", 3)     # Primera letra en mayúscula