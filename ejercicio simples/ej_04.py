new_planet = ''
planets = []

while new_planet.lower() != 'fin':
    if new_planet:planets.append(new_planet) #si newplanet existe, continua hacia la carga de ese planeta en la lista planetas a traves de .append
    new_planet = input("ingrese nuevo planeta o si termino ingrese fin: ")
    
print(planets)
