#______ function leer_______

def leer():
	n = int(input("Un valor="))

	return n

#______ function generarar primo...._______

def primos():
	conta=0
	suma =0

	while 3>conta:
		n = leer()
		c=0
		for i in range(1,n+1):
			if n % i==0:
				c = c + 1
		if c==2:
			#return True
			suma=suma + n
		conta = conta + 1
	return suma		


#______ function main_____
r=primos()
print("la suma es =", r)
