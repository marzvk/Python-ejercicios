edad = int(input("ingrese su edad:"))
pre_4_18= 5
pre_18_mas= 10
if edad < 4:
    fg = 0
elif edad < 18:
    fg = pre_4_18
else:
    fg = pre_18_mas

print(f'debe pagar: {fg:.2f} euros')

