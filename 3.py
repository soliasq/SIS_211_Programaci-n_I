#______ function leer_______

def leer():
	n=int(input("Un valor="))
	m=int(input("Un valor="))
	return n,m

#______ function suma, resta...._______

def suma(x,y):
	return x+y
def resta(x,y):
	return x-y
def multiplica(x,y):
	return x*y	
def division(x,y):
	if y == 0:
		print(" Math Eerror")
	else:
		return x/y
def raizCua(x,y):
	return (x**(0.5)),(y**(0.5))
def potencia(x,y):
	return x**y			
def mostrar(x,y):
	print (x,y)

#______ function main_____


n,m = leer()
res = suma(n,m)
mostrar(" suma:",res)
res = resta(n,m)
mostrar(" Resta:",res)
res = multiplica(n,m)
mostrar(" multiplicacion:",res)
res = division(n,m)
mostrar(" division:",res)
res = potencia(n,m)
mostrar(" potencia:",res)

res1,res = raizCua(n,m)
mostrar( f" raiz={n}:",res1)
mostrar( f" raiz={m}:",res)

