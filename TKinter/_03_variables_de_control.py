import tkinter as tk

ventana = tk.Tk()

# # # # STRINGVAR   <<<<<<<<<

texto = tk.StringVar(value='hola mundo')
# print(texto)    # da py var
print(texto.get())
texto.set('nuevo texto')  # con set cambiamos el texto
print(texto.get())

# agregar widget

entrada = tk.Entry(
    ventana, textvariable=texto)  # entry recibe el texto con textvariable
entrada.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()


def actualizar_etiqueta(*args):
    etiqueta.config(
        text=texto.get())  # recibe el texto del entry y con trace lo replica


texto.trace(
    "w", actualizar_etiqueta
)  # metodo TRACE detecta cuando hay un cambio en el valor de variable

# # # # # # >>>>>>>>>    INTVAR  ---  ENTERO   <<<<<<<<<<<

entero = tk.IntVar(value=40)
print(entero.get())

opcion1 = tk.Radiobutton(ventana, text='opc 1', variable=entero,
                         value=1)  # boton,recibe el entero de variable
opcion1.pack()
opcion2 = tk.Radiobutton(ventana, text='opc 2', variable=entero,
                         value=12)  # con el trace cambia al value
opcion2.pack()


def actualizar(*args):
    print(entero.get())


entero.trace_add("write", actualizar)

# # # # # # # # # # # DOUBLEVAR , FLOAT  <<<<<<<<< < < < < < << <

decimal = tk.DoubleVar(value=3.14)

control_deslizado = tk.Scale(ventana,
                             variable=decimal,
                             from_=0,
                             to=10,
                             resolution=0.01,
                             orient=tk.HORIZONTAL)
control_deslizado.pack()

### # # # # # # # ##  BOOLEANO <<<<<<<<

booleano = tk.BooleanVar(value=True)

casilla = tk.Checkbutton(ventana, text='aceptar', variable=booleano)
casilla.pack()


def definir(*args):
    print(booleano.get())


booleano.trace_add('write', definir)

ventana.mainloop()
