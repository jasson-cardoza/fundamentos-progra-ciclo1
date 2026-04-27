# 5. Validación de contraseña
# Con while, pide una contraseña hasta que sea correcta.
# Usa if para verificar si coincide.
# Después, usa for para mostrar cuántos intentos fallidos hubo.

correcta = "1234"
intentos_fallidos = 0

while True:
    contraseña = input("Ingrese la contraseña: ")
    
    if contraseña == correcta:
        break
    else:
        intentos_fallidos += 1

for i in range(intentos_fallidos):
    print("Intento fallido")