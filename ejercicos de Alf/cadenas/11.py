producto= input("ingrese nombre de producto: ")
precio= float(input("ingrese precio del producto: "))
cantidad= int(input("ingrese numero de unidades: "))
print(f'El producto {producto} su precio es: {precio:09.2f}, con {cantidad:03} unidades. El coste total es: {(precio*cantidad):011.2f}')
