def leer():
    n = int(input("Un valor="))
    return n

#______ function para generar vector _______
def llenar(n):
	V = []
	for i in range(n):
		x=leer()
		V.append(x)
	return V

def duplicar(V,n):
	suma=0
	for i in range(n):
		if i % 2 == 0:
			pass
		else:
			doble=V[i]
			suma=doble+doble 
			V[i]=suma
			
	return V	
def mostrar(V, n):
    for i in range(n):
        print(V[i],end=",")
    print()    
	

#______ function main _______



print("diminsion de vector")
n = leer()
print("Ingrese valores para vector : ")
vector = llenar(n)
nvector = duplicar(vector,n)
print("el doble del posiciones imparessdel vector : ")
mostrar(nvector,n)
