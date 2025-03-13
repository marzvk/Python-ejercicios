num= int(input("ingrese numero para saber si es primo: "))
for i in range(2,num): # desde 2 hasta uno menos q el mismo num, 
	if num % i == 0: # numero primo se divide por 1 y por si  mismo
		print(f'no es primo {i} es divisor')
		break
else:
		print("es un numero primo")
