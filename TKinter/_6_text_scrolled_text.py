import tkinter as tk
from tkinter.scrolledtext import ScrolledText

ventana = tk.Tk()
texto = tk.Text(ventana,
                width=40,
                height=5,
                wrap="word",  # wrap, al final de la linea se corta por palabra y no letra
                bg='lightgray', # background
                fg='black',  # foreground, color de la letra
                padx=10,
                pady=8,
                font=(12))
texto.insert("1.0", "hola, editor texto")  # primera linea de texto
texto.insert("end", "\n\ntexto resaltado", # desde primer linea, dos enter y sigue el texto
             "resaltado")  # etiqueta esta linea con la palabra  "resaltado"
texto.tag_configure("resaltado",
                    background='yellow')  # da un detalle al texto etiquetado

contenido = texto.get("1.0", "end")
print(contenido)

# texto.delete(1.0,'end')

texto.pack()

texto_desplazable = ScrolledText(ventana)
texto_desplazable.pack()



ventana.mainloop()
