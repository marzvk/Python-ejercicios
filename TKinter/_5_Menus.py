import tkinter as tk

ventana = tk.Tk()

menubuton = tk.Menubutton(ventana, text='archivo')
# menubuton.pack()

menu = tk.Menu(menubuton)
menubuton.config(menu=menu)

menu.add_command(label='Abrir')
menu.add_command(label='Guardar')


def abrir_archivo():
    print('archivo abierto')


menu.add_command(command=abrir_archivo, label='abrir impresion'
                 )  # cada vez q se aprieta el boton llama a la funcion

# # # #  > > > > > > > > > > BARRA MENU < < < < < < < < < <

barra_menu = tk.Menu(ventana)  # objeto barra menu, de la clase Menu
ventana.config(menu=barra_menu)

elemento_menu = tk.Menu(barra_menu)  # crea elemento en el menu
barra_menu.add_cascade(label='Actividad 1', menu=elemento_menu)

elemento_menu.add_command(label='nuevo')
elemento_menu.add_command(label='ver')
elemento_menu.add_separator()
elemento_menu.add_command(label='salir')

# anadir un menu editar a la barra de menu
editar_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Editar', menu=editar_menu)

# aniadir opciones al menu editar

editar_menu.add_command(label='Deshacer')
editar_menu.add_command(label='Reahacer')

# ------------> > > > > > MENU CONTEXTUAL -- MENU CON CLICK DERECHO < < < < < < ---------------------


def mostrar_menu_contextual(
        evento_esperado
):  # el evento que espera para iniciar es el click derecho
    menu_contextual.tk_popup(evento_esperado.x_root, evento_esperado.y_root)
    # poput sale el menu en el lugar x , y . donde se da el evento


menu_contextual = tk.Menu(ventana, tearoff=0)
# con tearoff en 0 la ventana q sale no se puede mover, con valor en 1 se puede desplazar

menu_contextual.add_command(label='cortar')
menu_contextual.add_command(label='copiar')
menu_contextual.add_command(label='pegar')

# ventana.bind("<Button-3>", mostrar_menu_contextual)
# puede alternar el uso con la linea 73 comentada

# genera el evento esperado, el click en boton 3 llama a la funcion

# # ------------->>>>>>> MENU CONTEXTUAL ASOCIADO A UN ENTRY <<<<<<<<<-------------

entrada = tk.Entry(ventana)
entrada.pack()

# solo se va a modicar el evento anterior, ahora el evento solo funciona adentro del entry

entrada.bind("<Button-3>", mostrar_menu_contextual)
# para usar alternar con la linea 61 comentada

ventana.mainloop()
