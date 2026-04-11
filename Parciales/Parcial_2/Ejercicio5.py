# Ejercicio 5
# 1. Inicia con la cadena "pYTHON".
# 2. Invierte las mayusculas por minusculas y las minusculas por mayusculas.
# 3. Alinea este nuevo texto hacia la izquierda en un espacio de 15 caracteres, rellenando los espacios vacios con asteriscos ("*").

texto="pYTHON";
print(texto);
texto= texto.swapcase();
print(texto);
texto=texto.ljust(15,"*");
print(texto);
