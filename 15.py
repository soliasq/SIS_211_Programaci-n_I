def leer():
	n = int(input("Un valor="))
	return n

#______ function generar..._______
def sumaDig():
	contarIgual=0
	primerDig=0
	n = leer()
	nOriginal = n
	contarIgual=0

	while nOriginal >= 10:
		nOriginalg = nOriginal //10
		print(nOriginal)
	primerDig = nOriginal	
	print(f"El primer dígito es: {primerDig}")
	
#______ function main_____
sumaDig()