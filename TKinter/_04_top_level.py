from tkinter import *

# # # # # # # TOP LEVEL ---- VENTANA INDEPENDIENTE A LA VENTANA PRINCIPAL

ventana = Tk()

ventana.title('principal')
ventana.geometry("600x400")

ventana_toplevel = Toplevel(ventana)
ventana_toplevel.title('top level')
ventana_toplevel.geometry("300x200+50+50")
# el 300 x 200, es ancho y alto, y el 50 + 50 el el desplazamiento de origen
# de la ventana al aparecer, 50 px en eje x y 50 px en eje y


def abrir_ventana_top_level():
    ventana_toplevel = Toplevel(ventana)
    ventana_toplevel.title('top level')
    ventana_toplevel.geometry("300x200+50+50")
    label = Label(ventana_toplevel, text=' ventana toplevel')
    label.pack()


def cerrar_ventana_top_level(param):
    param.destroy()


boton = Button(ventana,
               text='Abrir ventana top level',
               command=abrir_ventana_top_level)
boton.pack()

boton_cerrar = Button(
    ventana,
    text='cerrar ventana top level',
    command=lambda: cerrar_ventana_top_level(ventana_toplevel))
boton_cerrar.pack()
# solo cierra la primer ventana generada, no la de el boton que arma otra ventana externa

ventana.mainloop()
