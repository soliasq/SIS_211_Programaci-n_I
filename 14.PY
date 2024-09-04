#______ function leer_______
def leer():
	n = int(input("Un valor="))
	return n

#______ function generar..._______
def sumaDig():

	res = 0
	contar = 1
	while 3>=contar: # pide 3 numero verificamos
		n = leer()
		if n>0:
			while n > 0:
			    dig = n % 10
			    if dig % 3==0:
				    res = (res * 10) + dig 
			    print(dig ,end = ",")
			    n = n // 10 
			print (f"la suma es= {res}")
			

		else:
			print ( "el numero debe ser mayor de cero")
		contar = contar + 1  
#______ function main_____
sumaDig()