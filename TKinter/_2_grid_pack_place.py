import tkinter as tk

# # # # # # # FORMAS DE ORDENAR ELEMENTOS : << GRID >> ,<< PACK >>, << PLACE >> 

ventana1 = tk.Tk()

# -------------------- <<<<<<<<<<<<<<       GRID  >>>>>>>>>> ------------------

# label1 = tk.Label(ventana1, text='etiqueta 1')
# label1.grid(row=0, column=0,padx=10,pady=10)    # lo iniciamos con el grid, en vez del pack() que se venia usando

# label2 = tk.Label(ventana1, text='etiqueta 2')
# label2.grid(row=1, column=0,padx=10,pady=10) 
# ----------------- ---------------- ---------------


# label1 = tk.Label(ventana1, text='etiqueta 0.0')
# label1.grid(row=0, column=0,padx=10,pady=10) 

# label2 = tk.Label(ventana1, text='etiqueta 0.1')
# label2.grid(row=0, column=1,padx=10,pady=10)

# label3 = tk.Label(ventana1, text='etiqueta 1.0')
# label3.grid(row=1, column=0,padx=10,pady=10) 

# label4 = tk.Label(ventana1, text='etiqueta 1.1')
# label4.grid(row=1, column=1,padx=10,pady=10) 


# --------------- <<<<<<   PACK  >>>>>>> ------------------

# por default el pack ordena elementos de forma vertical, pero se los puede acomodar en forma horizontal

label1 = tk.Label(ventana1, text='etiqueta 1')
label2 = tk.Label(ventana1, text='etiqueta 2')

# label1.pack()
# label2.pack()

# frame_botones =tk.Frame(ventana1)
# frame_botones.config(background='Green',pady=10)     # pading eje y de 10 px
# frame_botones.pack(pady=10)

# boton1 =tk.Button(frame_botones,text='boton 1')
# boton1.pack(side='left',padx=5)         # posiciona el boton a la izquierda

# boton2 =tk.Button(frame_botones,text='boton 2')
# boton2.pack(side='left',padx=5)       # este a la izquierda del anterior

# boton3 =tk.Button(frame_botones,text='boton 3')
# boton3.pack(side='left',padx=5)

# # # # # # # ----->>>  PLACE <<< , COMO SU NOMBRE DICE POR UBICACION EN LA VENTANA, POR PIXELES

# label1.place(x=50, y=50)    # tambien se puede usar relativamente con relx = 0.25 -->> 25% en eje x
# label2.place(x=100, y=100)
# con el place lo iniciamos

ventana1.mainloop()