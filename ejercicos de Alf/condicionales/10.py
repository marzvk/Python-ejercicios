piza= "mozarella, tomate"
pe= input("ingrese que piza quiere: (veg o no veg) :")
if pe == "veg":
    ingredientes = input("elija un ingrediente vegetariano: pimiento o tofu: ")
else:
    ingredientes = input("elija ingrediente no vegetariano: peperoni , jamon o salmon: ")

print(f'La piza elegida es {pe} y tiene {piza} y {ingredientes}.')
    
        
