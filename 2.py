#______ function leer_______

def leer():
	n=int(input("Un valor="))
	return n

#______ function verificar_______

def verifica(x):
	a=1
	b=2
	if n<0:
		print("Valor negativo")
	elif n==0:
		print("Valor Nulo")
	else:	
		print("Valor Posetivo")
#______ function main_____

n=leer()
verifica(n)