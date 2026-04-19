# Ejercicio 10:
# Pide usuario y contraseña. Si ambos coinciden con valores predefinidos, muestra "Acceso permitido", de lo contrario "Acceso denegado".

usuario = input("Ingresa el usuario: ");
contraseña = input("Ingresa la contraseña: ");

if usuario == "admin" and contraseña == "Gokussj1":
    print("Acceso permitido");
else:
    print("Acceso denegado");