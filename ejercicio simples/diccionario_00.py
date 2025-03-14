planet = {'name': 'Earth','moons': 1} #diccionario, primer elemento es una clave 
                                     # el segundo es el valor
print (planet)
print(planet.get('name')) # acceder a un valor a traves de su clave
print(planet['name'])  # mismo procedimiento que el anterior
planet.update({'name': 'Makemake'}) # modifica el valor de la clave, o planet['name'] = 'Makemake'

planet.update({'name': 'Jupiter','moons': 79}) # modifica valores
print(planet)
planet['orbital_period'] = 4333 # agrega una clave desde afuera
print(planet)
planet.pop('orbital_period') # .pop para quitar una clave
print(planet)
planet['diametro en km'] = {'polar': 133709,'equatorial': 142984} # agrega otro diicionario
print(planet)                                               # adentro del ya existente 

print(f'{planet["name"]} polar diameter: {planet["diametro en km"]["polar"]}')
#para buscar valor en diccionario anidado, encadena corchetes el primero es clave el segundo el valor
