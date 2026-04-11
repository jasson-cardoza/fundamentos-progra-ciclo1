# Ejercicio 2
# 1. Toma la cadena de texto "Su nombre"".
# 2. Convierte el texto para que la primera letra de cada una de las palabras este en mayúscula.
# 3. Reemplaza la palabra "Su nombre" por "Su apellido" en el nuevo texto generado.


texto = "jasson cardoza"; #dejo mis nombres en minuscula para luego prbrar que el title funciona
texto = texto.title();
print(texto);
texto = texto.replace("Jasson Cardoza", "Cardoza Jasson");
print(texto);