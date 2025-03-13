num = int(input("ingrese altura del triangulo: "))
for i in range(1,num+1,2):
	for j in range(i,0,-2): # detrimento desde i hacia 0 en cada j con salto -2
		print(j,end="\t") #imprime cada devolucion de la linea con un salto de tab
	print("") # imprime salto de linea
