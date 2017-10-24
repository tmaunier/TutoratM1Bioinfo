def fibonacci(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibonacci(n-2)+fibonacci(n-1)
print ("Pour quelle valeur de n voulez-vous calculer la suite de fibonacci ?")
n=input()
print(fibonacci(n))    
    
