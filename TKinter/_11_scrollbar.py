import tkinter as tk

ventana = tk.Tk()

texto = tk.Text(ventana)

scrollbar = tk.Scrollbar(ventana, bg='pink')
scrollbar.pack(side='right',
               fill='y')  # barra a la derecha y con movimiento eje y

scrollbar.config(
    command=texto.yview
)  # yview permite q cuando se mueva la barra de desplazamiento el texto que se lee tb se mueva
texto.config(
    yscrollcommand=scrollbar.set
)  # set hace q la barra se mantenga en la posicion que uno la deja cuando se mueve
texto.pack(
    side='left', fill='both', expand=True
)  # texto inicia a la izq, se llena toda la pantalla a medida que se expande

ventana.mainloop()
