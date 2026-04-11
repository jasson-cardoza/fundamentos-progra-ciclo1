# Ejercicio 4
# 1. Toma la palabra "CANTANDO".
# 2. Convierte toda la cadena a letras minusculas.
# 3. Elimina el sufijo "ando" de la palabra resultante y encuentra en que indice (posicion) quedo la letra "t".

texto="CANTANDO";
print(texto);
texto=texto.lower();
print(texto);
texto=texto.removesuffix("ando");
print(texto);

