planets_moons = {'mercury': 0,
'venus': 0,
'earth': 1,
'mars': 2,
'jupiter': 79,
'saturn': 82,
'uranus': 27,
'neptune': 14,
'pluto': 5,
'haumea': 2,
'makemake': 1,
'eris': 1}

total_planets= len(planets_moons.keys())
moons = planets_moons.values()
print(total_planets)
total_monns = 0
for moon in moons:
    total_monns=total_monns+moon
print(total_monns)
promedio= total_monns/total_planets
print(f' el promedio de lunas por planeta es de : {promedio}')
