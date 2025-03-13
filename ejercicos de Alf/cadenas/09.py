fecha= input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa")
print('dia', fecha[:2])
print('mes', fecha[3:5])
print('anio', fecha[6:]) 
print()

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')] # busca desde inicio hasta primer barra
mesaño = fecha[fecha.find('/')+1:] #busca desde 1 barra hasta el final
mes = mesaño[:mesaño.find('/')] # busca desde la 1 barra hasta la segunda o sea (mes)
año = mesaño[mesaño.find('/')+1:] # desde la ultima barra o sea el anio hasta el fin
print('Día', dia)
print('Mes', mes)
print('Año', año)
