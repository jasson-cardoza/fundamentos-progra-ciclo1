# Ejercicio 2:
# Solicita la edad de una persona y muestra si es menor de edad, mayor de edad o adulto mayor (60 o más).

edad = float(input("Ingresa su edad: "));

if edad >= 1 and edad <=17:
    print("Es menor de edad");
elif edad >=18 and edad<=59:
    print("Es mayor de edad");
elif edad >= 60 and edad<=105:
    print("Es un adulto mayor");
else:
    print("Inngrese un número valido");