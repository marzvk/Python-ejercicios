renta= float(input("ingrese su renta anual"))
if renta < 10000:
    impuesto=0.05
elif renta < 20000:
    impuesto=0.15
elif renta < 35000:
    impuesto=0.2
elif renta < 60000:
    impuesto=0.3
else:
    impuesto=0.45
print(f'le corresponde {renta*impuesto} $ de impuestos')
