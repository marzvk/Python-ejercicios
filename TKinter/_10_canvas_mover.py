import tkinter as tk


def iniciar_arrastre(evento):
    global objeto_seleccionado
    objeto_seleccionado = canvas.find_closest(evento.x, evento.y)


def terminar_arrastre(evento):
    global objeto_seleccionado
    if objeto_seleccionado:
        x, y = evento.x, evento.y
        canvas.move(objeto_seleccionado,
                    x - canvas.coords(objeto_seleccionado)[0],
                    y - canvas.coords(objeto_seleccionado)[1])
        objeto_seleccionado = None


ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=500, height=300)
canvas.pack()

objeto_seleccionado = None

rectangulo = canvas.create_rectangle(50,
                                     50,
                                     150,
                                     150,
                                     fill='green',
                                     outline='black',
                                     width=2,
                                     tags='rectangulo')

canvas.tag_bind('rectangulo', "<ButtonPress-1>", iniciar_arrastre)
canvas.tag_bind('rectangulo', "<ButtonRelease-1>", terminar_arrastre)

ventana.mainloop()
