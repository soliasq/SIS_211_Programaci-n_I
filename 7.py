#______ function leer_______

def leer():
	n = int(input("Un valor="))
	return n
#______ function generarar primo...._______

def pi():
	signo= (-1)*1
	cons=4
	conta=0
	suma =0
	impares=1
	n = leer()
	while n>conta:
		#print(impares)
		#print(f"{cons}/{impares}")
		if conta %2==0:
			suma=suma+(cons/impares)
		else:
			suma=suma -(cons/impares)
		impares= impares+2

		conta =conta +1
	
	return suma		
#______ function main_____
r = pi()
print("el pi es =", r)
