# Ejercicio 8
# 1. Define un bloque de texto de 3 lineas usando comillas triples (puedes usar un fragmento del poema de la guia).
# 2. Cuenta cuantas veces aparece la letra "a" en todo el bloque de texto.
# 3. Divide el bloque de texto por sus saltos de linea (splitlines) para convertirlo en una lista de oraciones independientes.

texto = """Es porque un pajarito de la montaña ha hecho
en el hueco de un árbol, su nido matinal, que el árbol amanece con música en el pecho,
como que si tuviera corazón musical."""
conteo = "La cantidad de letras 'a' en el texto son:" , texto.count("a")
lineas = texto.splitlines()
print(conteo)
print(lineas)