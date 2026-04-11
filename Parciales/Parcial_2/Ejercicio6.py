# Ejercicio 6
# 1. Toma el texto "Su nombre".
# 2. Aplica el método de normalización fuerte (casefold) para prepararlo para una comparación ignorando mayúsculas.
# 3. Verifica si el texto resultante está compuesto únicamente por caracteres alfabéticos (letras) devolviendo un valor booleano.

texto = "Jasson Cardoza";
print(texto);
texto = texto.casefold();
print(texto);
resultado = texto.isalpha();
print(resultado); #da falso porque mi nombre esta separado por un espacio
                  #Si no tuviera espacio sale true