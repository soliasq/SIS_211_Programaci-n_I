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

def verPrimo(V,n):
	suma = 0
	c=0
	for i in range(n):
          
		primo = V[i]
		c=0
		for j in range(1,primo+1):
			if primo % j == 0:
				c = c + 1
		if c == 2:
			suma = suma + primo		
		#V[i] = suma
			
	return suma	
def mostrar(V, n):
    for i in range(n):
        print(V[i],end=",")
    print()    
def verSumaPrimo(nvector):
	c=0
	for j in range(1,nvector +1):
		if nvector % j == 0:
			c = c + 1
	if c == 2:
		print(f"La suma es un numero primo")
	else:			
		print(f"La suma no es un numero primo")

#______ function main _______



print("dimension de vector")
n = leer()
print("Ingrese valores para vector : ")
vector = llenar(n)
nvector = verPrimo(vector,n)
print("la suma de los primos  en el vector es : ",nvector)

verSumaPrimo(nvector)

mostrar(vector,n)
