#______ function leer_______

def leer():
	n = int(input("Un valor="))
	m = int(input("Un valor="))
	nn=int(input("Un valor="))
	return n,m,nn
#______ function generarar primo...._______

def cubo(a,b,c):
	 a1 = a*a*a
	 b1 = b*b*b
	 c1 = c*c*c
	 raiz( a,b1,c1)
def raiz( a,b,c):
	suma=0
	suma= (a+b+c)**0.5
	print("la raiz",suma)
#______ function main_____
x,y,z = leer()
cubo(x,y,z)
