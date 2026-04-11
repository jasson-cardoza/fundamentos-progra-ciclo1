# Ejercicio 12 
# 1. Toma el nombre de archivo "Sunombre.txt".
# 2. Remueve el sufijo ".txt" y posteriormente remueve el prefijo "ING. ".
# 3. Toma el texto que quede limpio, convertido a minúsculas.

texto = "ING.Jasson_Cardoza.txt";
texto = texto.removesuffix(".txt");
texto = texto.removeprefix("ING.");
texto = texto.lower();
print(texto);