# Ejercicio 5
# Para cumplir con la normativa de privacidad, debes transformar los nombres de los usuarios, invirtiendo su orden y formateando la estructura de las letras. Pide al usuario su nombre completo (Nombre y Apellido). Conviértelo en una lista usando .split() y utiliza Slicing con paso negativo[::-1]) para que el apellido aparezca antes que el nombre en una nueva lista.


nombre_completo = input("Ingrese su nombre completo: ")

lista_nombres = nombre_completo.split()
lista_invertida = lista_nombres[::-1]

for palabra in lista_invertida:
    for letra in palabra:
        print(letra, end=".")
    print()