nombre= input("ingrese su nombre")
sexo= input("ingrese su sexo: M o H")
if sexo == "M":
    if nombre[0].lower() <= "m":
        print("pertenece al grupo A")
    else:
        print("pertene al grupo B")
else:
    if nombre[0].lower() >= "n":
        group= "A"
    else :
        group= "B"
    print(f'Su grupo es {group}')

    
