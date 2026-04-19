# Ejercicio 5:
# Solicita dos números y una operación (+, -, *, /) y realiza el cálculo usando if, elif y else.

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

if operacion == "+":
    print(numero1 + numero2);
elif operacion == "-":
    print(numero1 - numero2);
elif operacion == "*":
    print(numero1 * numero2);
elif operacion == "/":
    if numero2 != 0:
        print(numero1 / numero2);
    else:
        print("No se puede dividir entre cero");
else:
    print("Operación no válida");