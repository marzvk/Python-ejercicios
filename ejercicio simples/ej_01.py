"""Escribir un programa que pregunte el nombre del usuario en la consola y 
después de que el usuario lo introduzca muestre por pantalla 
la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido."""

name = input('cual es su nombre: ')
#print('! Hola ' + name +'!')

text = '!Hola {nombre}!'
print(text.format(nombre = name))


