materias = ['matematica', 'quimica', 'lengua', 'historia', 'fisica']
notas = []
for materia in materias:
    nota = input("ingrese la nota que saco en: " + materia)
    notas.append(nota)
for i in range(len(materias)):
    print(f"En {materias[i]} sacaste: {notas[i]}")
#for par in enumerate(materias):
#print(par)
# print(f"En {par[1]} sacaste: {notas[par[0]]}")
