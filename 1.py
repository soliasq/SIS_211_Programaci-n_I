def leer():
	n=int(input("Un valor="))
	return n
def serie(x):
	a=1
	b=2
	if n<0:
		print("Incorrect input")
	elif n==0:
		print(0)
			
	elif n==1:
		print(a+b)
	else: 
		for i in range(1,x+1):
			c=a+b
			a=b
			b=c
			print(b,end=', ')
n=leer()
serie(n)
