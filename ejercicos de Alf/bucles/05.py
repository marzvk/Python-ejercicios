cantidad = float(input("ingrese cantidad a invertir: "))
interes = float(input("ingrese intees anual: "))
anios = int(input("ingrese cantidad de anios: "))
i = 1
while i <= anios:
	print(f'{(cantidad*interes)/100} interes en {i} anios')
	cantidad = ((cantidad*interes)/100+cantidad)
	i += 1
