cantidad=float(input("cuanto desea invertir? "))
interes=float(input("que interes anual quiere? "))
anos=float(input("cuantos anos invertira? "))
capital=((cantidad*interes*anos)/100)
print(f'el capital total obtenido es: {capital+cantidad}')
