import tkinter as tk

# # # # # >>>>>>>>> EJEMPLO CORTAR PEGAR COPIAR ,<< < < < < < < <  <

ventana = tk.Tk()
# def copiar():
#     texto.event_generate("<<Copy>>")  # se genera evento copiar al texto


# def cortar():
#     texto.event_generate("<<Cut>>")  # se genera el evento cortar en el texto


# def pegar():
#     texto.event_generate("<<Paste>>")

# # texto = tk.Text(ventana)
# # texto.pack()

# # boton_copiar = tk.Button(ventana, text='copiar', command=copiar)
# # boton_copiar.pack()  # boton con titulo copiar que llama a la funcion copiar

# # boton_cortar = tk.Button(ventana, text='cortar', command=cortar)
# # boton_cortar.pack()

# # boton_pegar = tk.Button(ventana, text='pegar', command=pegar)
# # boton_pegar.pack()

# DESCOMENTAR DESDE LINEA 6 HASTA ^^^^^^^^^^^^^^^^

# # # # # # # >>>>>>>>>>>>  GUARDAR ARCHIVO. ABRIR ARCHIVO   <<<<<<<<<<<<<

from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfile
# askopenfile es para abrir un archivo.  ask save as file es para guardar


def abrir_archivo():
    archivo = askopenfilename()  # metodo para abrir archivo
    if archivo:  # cuando selecciono archivo
        texto_desplazable.delete(
            1.0, 'end')  # borro todo lo que existe en el texto desplazable
        with open(archivo, 'r') as file:  # leemos y abrimos el archivo
            texto_desplazable.insert(
                1.0, file.read())  # insertamos el archivo desde primer lugar


def guardar_archivo():
    archivo = asksaveasfile()
    if archivo:
        with open(archivo, 'w') as file:
            file.write(
                texto_desplazable.get(1.0, 'end')
            )  # escribe lo hecho en el archivo desde el inicio hasta su linea final


texto_desplazable = ScrolledText(ventana, wrap='word')
texto_desplazable.pack(
    expand=True, fill='both'
)  # se puede expandir, y fill both llena las letras cuando se expande, o sea acompania la pantalla

boton_abrir = tk.Button(ventana, text='abrir', command=abrir_archivo)
boton_abrir.pack(side='left')

boton_guardar = tk.Button(ventana, text='guardar', command=guardar_archivo)
boton_guardar.pack(side='left')

ventana.mainloop()
