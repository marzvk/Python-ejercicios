import tkinter as tk
from tkinter import ttk

# # # # >>>>>>>>>>>>>>>>>>>  LISTBOX  <<<<<<<<<<<<<<<<<

ventana = tk.Tk()
ventana.title('ejemplo listbox')

listbox = tk.Listbox(ventana,
                     width=30,
                     height=10,
                     font=('Arial', 12),
                     fg='blue',
                     bg='#ABA296')
# selectmode=tk.MULTIPLE)
# # >>>>> SELECCIONA MULTIPLES ELEMENTOS  <<<<<<

listbox.insert(tk.END, "elemento 1 papas"
               )  # primer elemento es el indice de orden, segundo titulo
listbox.insert(tk.END,
               "elemento 2 cebollas")  # tk.END agrega elemento al final
listbox.insert(tk.END, "elemento 3 sandias")
listbox.insert(0, "elemento 0 huevos")  # se puede cargar por valores el indice

# listbox.delete(3)

listbox.pack()


def on_seleccionar(evento_dado):
    indice = listbox.curselection()  # curselection lee el indice de la lista
    elemento = listbox.get(indice)
    print(f'el valor del indice es {indice} : {elemento}')


listbox.bind(
    "<<ListboxSelect>>", on_seleccionar
)  # primer argumento de donde toma el evento, segundo llama funcion


def on_click(evento):
    print('hizo click en listbox')


listbox.bind(
    "<Button-1>", on_click
)  # bind,lee evento click 1 que es click izquierdo, lo pasa a la funcion on click que
# requiere un evento como parametro

# # # # >>>>>> >> > >>  >> COMBOBOX <<<<< < < < <  < <

combobox = ttk.Combobox(ventana,
                        width=30,
                        font=('arial', 12),
                        foreground='green',
                        background='orange')
combobox.pack()

elementos = ['ele 1', 2, 'elem 3']
combobox['values'] = elementos

# elementos[1] = 'elem 2'
# combobox['values']= elementos     # modificar valores por indice, luego se modifica el combobox


def on_selec_combobox(evento):
    valor_elegido = combobox.get()
    print(f'selecciono: {valor_elegido}')


combobox.bind("<<ComboboxSelected>>", on_selec_combobox)

ventana.mainloop()
