def leer():
    n = int(input("Un valor="))
    return n

#______ function para generar vector _______
def llenar(n):
	V = []
	for i in range(0, n):
		x=leer()
		V.append(x)
	return V

def primoVer(V,n):
	suma=0
	var=0
	for i in range(0,n):
#		V[i]+=30
		suma=0
		var=0
		var=V[i]
		while var>0:
			nn=var%10 
			suma=suma+nn 
			var=var//10
		V[i]=suma			
	return V	
def mostrar(V, n):
    for i in range(0,n):
        print(V[i],end=",")
    print()    
	

#______ function main _______



print("diminsion de vector")
n=leer()
print("Ingrese valores para vector : ")
vector=llenar(n)
nvector=primoVer(vector,n)
print("la suma del nuevo vectors en cada posicion : ")
mostrar(nvector,n)
