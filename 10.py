#______ function leer_______

def leer():
	n = int(input("Un valor="))

	return n
#______ function generar..._______


def divisores(n):
	suma= 0
	for i in range(1,n+1):
		if n % i==0:
			print(i,end=",")
			suma=suma+i 
	return suma
def mostrar(a,b):
	print(a,b)
#______ function main_____
x = leer()
r=divisores(x)
mostrar("La suma es:",r)
