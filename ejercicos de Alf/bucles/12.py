# lee si una letra esta en una palabra y cuantas veces esta

frase = input("ingrese una frase: ")
letra = input("ingrese una letra: ")
cuenta = frase.count(letra)  # sintax = string.count(value, start, end)
print(f' la letra {letra} aparece un total de: {cuenta} veces')
