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

def factorial(V,n):
	suma = 0
	for i in range(n):
          
		fact = V[i]

		fa =1
		res= fact % 10

		for  j in range(1,res+1):
		 	fa = fa *j
		V[i] = fa
			
	return V	
def mostrar(V, n):
    for i in range(n):
        print(V[i],end=",")
    print()    
	

#______ function main _______



print("dimension de vector")
n = leer()
print("Ingrese valores para vector : ")
vector = llenar(n)
nvector = factorial(vector,n)
print("el factorial de l ultimo digto es : ")
mostrar(nvector,n)
