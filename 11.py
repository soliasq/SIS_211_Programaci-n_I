#______ function leer_______

def leer():
	n = int(input("Un valor="))
	return n
#______ function generar..._______

def multiplo(n):
	suma= 0
	mult=0
	for i in range(1,n+1):
		print(i*5,end=",")
		mult=mult+(i*5) 
		suma=suma+mult
	return mult
def mostrar(a,b):
	print(a,b)
#______ function main_____
n = leer()
r =multiplo(n)
mostrar("La sumaes:",r)