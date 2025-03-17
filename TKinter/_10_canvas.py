import tkinter as tk

ventana = tk.Tk()
canvas = tk.Canvas(ventana, width=500, height=300, bg='lightblue')

rectangulo = canvas.create_rectangle(50,
                                     50,
                                     150,
                                     100,
                                     fill='green',
                                     outline='black',
                                     width=2)
# inicia 50 px separado de inicio en eje x e y, luego tiene 150 ancho, y 100 alto

# canvas.move(rectangulo,100 ,100)   # mueve elemento 100 px en x, 100 en y

canvas.create_oval(200,
                   50,
                   300,
                   150,
                   fill='orange',
                   outline='yellow',
                   width=3,
                   dash=10)
# en este caso un circulo de 100 px

canvas.create_polygon(350,
                      50,
                      400,
                      100,
                      350,
                      150,
                      fill='blue',
                      outline='purple',
                      width=5)

canvas.create_polygon(450,
                      150,
                      450,
                      270,
                      300,
                      210,
                      300,
                      190,
                      fill='brown',
                      outline='black')
# a medida que uno genera las coordenadas x e y, se genera el punto, en orden que se cargan

canvas.create_line(10,
                   200,
                   200,
                   200,
                   fill='blue',
                   width=3,
                   dash=(5),
                   capstyle='round')

# CREAR TEXTO
canvas.create_text(250,
                   30,
                   text=' prueba texto',
                   fill='darkgreen',
                   font=('Courier', 12, 'italic'),
                   justify='center')

canvas.pack(fill='both',
            expand=True)  # se expande el canvas, y se rellena la ventana

ventana.mainloop()
