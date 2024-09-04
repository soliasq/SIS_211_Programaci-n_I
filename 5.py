#______ function leer_______

def leer():
	x = int(input("Un valor="))
	y = int(input("Un valor="))
	z = int(input("Un valor="))
	return x,y,z

#______ function generarar tabla...._______

def facto(x):
	fa=1
	for i in range(1,x+1):
		fa = fa*i
	return fa

def mostrar(x,y):
	print (x,y)

#______ function main_____
res=0
suma = 0
x,y,z = leer()
res = facto(x)
mostrar(f"factorial={x}",facto(x))
suma = suma+ res

res = facto(y)
mostrar(f"factorial={y}",facto(y))

suma =suma+ res
res = facto(z)
mostrar(f"factorial={z}",facto(z))
suma = suma+ res
print("la suma=",suma)