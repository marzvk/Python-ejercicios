"""Escribir un programa que pregunte al usuario por el número de horas 
trabajadas y el coste por hora. Después debe mostrar por pantalla 
la paga que le corresponde"""

horas_trabajadas = input ('Cual es el total de horas trabajadas ? ')
coste_hora = input('Cual es el costo de la hora ? ')
print(f"Total a cobrar: {float(horas_trabajadas) * float(coste_hora)} ")
