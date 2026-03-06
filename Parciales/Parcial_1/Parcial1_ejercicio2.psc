Algoritmo UnnumeroNegativo
	Suma = 0
	Repetir
		Escribir "Ingrese un número (negativo para salir):"
		Leer num
		Si num >= 0 Entonces
			Suma = Suma + num
		FinSi
	Hasta Que num < 0
	Escribir "La suma de los números positivos es: ", Suma
FinAlgoritmo