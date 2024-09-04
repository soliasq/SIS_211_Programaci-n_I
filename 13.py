#______ function leer_______
def leer():
	n = int(input("Un valor="))
	return n

#______ function generar..._______
def sumaDig(n):

	res = 0

	while n > 0:
	    dig = n % 10
	    res = res + dig 
	    print(dig,end=",")
	    n = n // 10 
	print (f"la suma es= {res}")  

	


#______ function main_____
n= leer()
sumaDig(n)

