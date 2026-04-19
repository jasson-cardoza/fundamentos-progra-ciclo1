# Ejercicio 3:
# Ingresa una nota del 0 al 10 y muestra:
# 9-10: Excelente
# 7-8: Bueno
# 6: Aprobado
# 0-5: Reprobado



nota = float(input("Ingresa su nota: "));

if nota >= 9 and nota <=10:
    print("Excelente");
elif nota >=7 and nota<=8:
    print("Bueno");
elif nota == 6:
    print("Aprobado");
elif nota >= 0 and nota<=5:
    print("Reprobado");
else:
    print("Porfavor ingrese su nota en escala del 1 al 10");