precio_pan=3.49
barras_ayer=int(input("cuantas barras de ayer se vendieron: "))
print(f'el precio de la barra es: {precio_pan}')
print("el pan del dia anterior tiene 60% de descuento")
coste_final=barras_ayer*(precio_pan*(1-0.6))
print(f'el coste final total de los panes de ayer es: {coste_final:.2f}')

