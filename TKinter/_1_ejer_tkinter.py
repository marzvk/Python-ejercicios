import tkinter as tk
import time
from random import *

## ---------------------
ventana = tk.Tk()         # iniciar ventana, llama a la clase tkinter y la genera
ventana.title('ejemplo')


# # # # LABEL

etiqueta = tk.Label(ventana, text='hola soy una etiqueta')
etiqueta.config(background='black',foreground='white',font=('Arial',22,))
etiqueta.pack()  # metodo para aniadir los objetos en la ventana

# # # # # # BUTTON   -------->>>>>>>> BOTONES 

boton = tk.Button(ventana, text='Presiona aqui')
boton.config(background='orange',foreground='blue',font=('Arial',16))
boton.pack()

# button = tk.Button(ventana1,
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# button.pack()

# BOTON GRANDE CON COLOR

def boton_presionado():
    print('presiono el boton, y yo te lo muestro')

def cambiar_texto():
    etiqueta.config(text='cambio el texto') ### aca se puede poner un random ?


boton.config(command=cambiar_texto)


# # # # ENTRY ------->>>>>  INPUT

entrada = tk.Entry(ventana) # adentro de ventana aparece el 
entrada.config(background='yellow',foreground='orange')
entrada.insert(0, 'Nombre')  # texto que va a apatecer en la solapa de muestra
entrada.pack()

###### GET ------>>>>> RECIBIR EL TEXTO INGRESADO

# texto = entrada.get()
# print(texto)

def aplicar_texto():
    texto = entrada.get()
    etiqueta.config(text=texto) # funcion cambia la etiqueta por lo q ingresa en el texto con get

boton_aplicar = tk.Button(ventana,text='aplicar texto', command=aplicar_texto)
# aqui con el command llama a la funcion aplicar texto
boton_aplicar.pack()

# # # # # # CALLBACK 

def on_click(event):
    print(' botonnnn')

buton = tk.Button(ventana, text=' has click aca')
buton.pack()
buton.bind("<Button-1>", on_click)  # aca buton 1 llama al uso del boton izquierdo del mouse. BIND lee eso
                                    # y lo usa con la funcion que imprime 
def presiono_tecla(event):
    if event.char == 'a':
        print('tecla a presionada')

ventana.bind("<KeyPress>", presiono_tecla)# BIND asocia eventos a las funciones q recibe como parametro 
# en el segundo parametro, aca asocia keypress, tocar tecla,hacia activar funcion imprime a cuando la presiono

def modif_tamanio_ventana(event):
    print(f'La ventana cambio de tamanio : {event.width} x {event.height}')
# ventana.bind("<Configure>",modif_tamanio_ventana) # con Configure accede a configuracion de ventana

def on_click_con_for(event):
    print(f'{event.widget['text']} presionado') # widget lee el boton del mouse que presiona. cuando el bind
    # lo llama mas abajo

botones = [tk.Button(ventana, text= f'Boton {i+1}') for i in range(3)]
# hace una lista de 3 botones con el numero con un for en lista

for buutton in botones:
    buutton.pack()
    buutton.bind("<Button-1>", on_click_con_for)

###### RADIO BUTTON --------------~>>>>>>>> ELEGIR UN BOTON

variable_control = tk.IntVar() ##### aqui se guarda el valor elegido en el boton

# opcion1 = tk.Radiobutton(ventana, text= 'opcion 1', variable= variable_control, value= 1)
# opcion2 = tk.Radiobutton(ventana, text= 'opcion 2', variable= variable_control, value= 2)
def cambiar_color():
    color_elegido = variable_control.get()
    if color_elegido == 1:
        ventana.config(background='Red')
    elif color_elegido == 2:
        ventana.config(background='Green')


opcion1 = tk.Radiobutton(ventana, text= 'Rojo', variable= variable_control, value= 1, command= cambiar_color)
opcion2 = tk.Radiobutton(ventana, text= 'Verde', variable= variable_control, value= 2, command= cambiar_color)

opcion1.pack()
opcion2.pack()

def mostrar_selecion():  # funcion que devuelve la opcion elegida en el boton
    print('opcion elegida: ',variable_control.get()) 

boton_selecion = tk.Button(ventana, text= 'mostrar seleccion', command=mostrar_selecion) # llama a la funcion
# boton_selecion.pack()

########## CHECKBUTTON ------>>>>>> VARIAS OPCIONES A LA VEZ

variable_check1 = tk.BooleanVar()   #   es necesario una variable por cada opcion a elegir
variable_check2 = tk.BooleanVar()   #   por eso se puede elegir mas de una opcion

# check1 = tk.Checkbutton(ventana, text= 'opcion 1',variable=variable_check1)
# check2 = tk.Checkbutton(ventana, text= 'opcion 2',variable=variable_check2)

# check1.pack()
# check2.pack()

def check_button_cambio():
    print('el check cambio')

# check1 = tk.Checkbutton(ventana, text= 'opcion 1',variable=variable_check1, command= check_button_cambio)
# check1.pack()

# # # # Ejemplo con DISABLED Y NORMAL ------->>>>>>>>> DESACTIVADO Y ACTIVADO

def habilitado():
    if variable_check1.get():
        boton_hab.config(state ="normal")
    else:
        boton_hab.config(state ="disabled")

boton_hab =tk.Button(ventana, text='boton habilitar: ejemplo para enviar todo',state='disabled')
check1 = tk.Checkbutton(ventana,text='habilitar boton',variable=variable_check1,command=habilitado) 

check1.pack()            # dependiendo del orden en que se cargue el .pack()
boton_hab.pack()         # es como aparece en la pantalla

#<<<<<<<<<<<          >>>>>>>>>>>>>>>>    MAINLOOP COMENTADO ABAJO
ventana.mainloop()