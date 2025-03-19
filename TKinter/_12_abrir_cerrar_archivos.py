import tkinter as tk
from tkinter import filedialog

ventana = tk.Tk()
ventana.title('Visor archivo de texto')


def abrir_archivo():
    ruta_de_archivo = filedialog.askopenfilename(     # metodo que abre el archivo, y se elige el tipo que
        filetypes=[('Archivos de texto',              # uno quiera
                    '*.txt'), ('Archivos tipo Python',
                               '*.py'), ('Todos los archivos', '*.*')])
    if ruta_de_archivo:
        with open(ruta_de_archivo,'r') as file_object:  # abre archivo y lo lee con 'r'
            contenido = file_object.read()    # pone el contenido leido en una variable
            texto_widget.delete(1.0, tk.END)  # borra lo que exista en el texto antes de insertar el archivo
            texto_widget.insert(tk.INSERT, contenido)


def guardar_archivo():
    ruta_de_archivo = filedialog.askopenfilename(     
        filetypes=[('Archivos de texto',              
                    '*.txt'), ('Archivos tipo Python',
                               '*.py'), ('Todos los archivos', '*.*')])
    if ruta_de_archivo:
        with open(ruta_de_archivo,'w') as file_object:
            contenido = texto_widget.get(1.0, tk.END)
            file_object.write(contenido)

# toma lo que hay en texto_widget, desde el inicio haste el fin. a ese contenido lo escribe en 
# file_object, y a eso lo lleva a traves de ruta de archivo hasta el archivo elegido


texto_widget = tk.Text(ventana, padx=10,wrap='word')
texto_widget.pack(expand=True, fill='both')

abrir_boton = tk.Button(ventana, text='Abrir Archivo', command=abrir_archivo)
abrir_boton.pack()

guardar_boton = tk.Button(ventana,text='Guardar Archivo', command= guardar_archivo)
guardar_boton.pack()

ventana.mainloop()