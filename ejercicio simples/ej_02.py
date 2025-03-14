"""Escribir un programa que pregunte el nombre del usuario y la edad,
almacenarlos en una constante/variable y luego imprimir el string 
"Hola, <nombre>! Tenes <edad> anos." """

nombres = input('cual es su nombre? ')
edads = input('cuantos anos tienes? ')

salida = "Hola {nombre} ! Tenes {edad} anos."
print (salida.format(nombre = nombres , edad = edads))

print(f"Hola {nombres.upper()} ! Tenes {float(edads):.2f} anos.")# upper hace mayuscula la primera
