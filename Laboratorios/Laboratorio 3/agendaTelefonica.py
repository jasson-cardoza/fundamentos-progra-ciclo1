# Agenda telefónica: for contactos, if buscar, while menú, select case opciones.

print("Escribe el numero de la opcion a elegir:")

contactos = {}

while True:
    print("1. Agregar")
    print("2. Buscar")
    print("3. Mostrar")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        numero = input("Número: ")
        contactos[nombre] = numero

    elif opcion == "2":
        nombre = input("Buscar nombre: ")
        if nombre in contactos:
            print(contactos[nombre])
        else:
            print("No encontrado")

    elif opcion == "3":
        for nombre in contactos:
            print(nombre, contactos[nombre])

    elif opcion == "4":
        break