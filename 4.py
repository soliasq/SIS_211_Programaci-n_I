#______ function leer_______

def leer():
	n=int(input("Un valor="))
	return n

#______ function generarar tabla...._______

def tabla(x):
	for i in range(1,11):
		print(f"{i}*{n}=",i*n )

#______ function main_____
n = leer()
tabla(n)
