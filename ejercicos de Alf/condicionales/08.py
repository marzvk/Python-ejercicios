punt= float(input("ingrese su puntuacion:"))
bonif = 2400
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
if punt == inaceptable:
    fg = "inaceptable"
elif punt == aceptable:
    fg = "aceptable"
elif punt >= meritorio:
    fg = "meritorio"
else:
    fg = " "
if fg != " ":
    print(f'su rendimiento es {fg},recibira: {punt*bonif} euros')
else:
    print("ingrese bien su puntuacion")
