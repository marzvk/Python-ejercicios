numeros = list()
for i in range(0, 6):
    num = input("ingrese numero de sorteo: ")
    numeros.append(int(num))

numeros.sort()
print(numeros)
