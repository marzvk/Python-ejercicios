precio= input("ingrese precio del producto con dos decimales: ")
print(precio[:-3],'euros y ', precio[-2:], 'centavos')

precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')
 # otra solucion con .find() busca la posicion exacta

