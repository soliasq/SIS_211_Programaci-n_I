#______ function leer_______

def leer():
	n = int(input("Un valor="))
	return n
#______ function generarar primo...._______

def pi():
	expo=3
	cons1=2
	conta=0
	suma =0
	n = leer()
	a=1
	b=1
	c=0
	while n>conta:
		c= a+b
		a=b
		b=c
		if cons1 %2==0:
			suma=suma+(b**expo/cons1)
			cons1=cons1+1
		else:
			suma=suma+(b**expo/cons1)
			cons1=cons1-1
		
		expo =expo+1

		conta =conta +1
	
	return suma		
#______ function main_____
r = pi()
print("el pi es =", r)
