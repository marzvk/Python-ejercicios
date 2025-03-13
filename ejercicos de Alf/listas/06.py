materias = ['matematica', 'quimica', 'lengua', 'historia', 'fisica']
desaprobadas = []
for materia in materias:
    nota = float(input("cuanto saco en:" + materia + "?"))
    if nota < 6:
        desaprobadas.append(materia)

print(f"Tienes que repetir:  {desaprobadas}")
