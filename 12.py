#______ function leer_______
def leer():
	n = int(input("Un valor="))
	return n
#______ function generar..._______
def palindromo(n):
	nn = n
	res = 0

	while n > 0:
	    dig = n % 10
	    res = (res * 10) + dig 
	    n = n // 10   

	
	if nn == res:
	    print(f"El número {nn} es un palíndromo. =={res}")
	else:
	    print(f"El número {nn} no es un palíndromo. =={res}")
#______ function main_____
n= leer()
palindromo(n)

