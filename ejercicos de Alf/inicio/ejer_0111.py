capital_inicial=int(input("cuanto tiene depositado: "))
i=0.04
capital_final_1=capital_inicial*(1+i)
cap_2=capital_final_1*(1+i)
cap_3=cap_2*(1+i)
print(f'el primer anio tendra: {capital_final_1:.2f}')
print(f'el segundo anio tendra: {cap_2:.2f}')
print(f'el tercer anio tendra: {cap_3:.2f}')

