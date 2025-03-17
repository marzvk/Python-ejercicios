import tkinter as tk
from PIL import ImageTk, Image
# con pil se pueden usar imagenes jpg

ventana = tk.Tk()
# imagen_pil_1 = Image.open('imagenes/pngwing.com.png')
# imagen_pil_1 = imagen_pil_1.resize((200, 200))
# imagen_tk_1 = ImageTk.PhotoImage(imagen_pil_1)
imagen_pil_2 = tk.PhotoImage(file='imagenes_y_txt/android-chrome-512x512.png')
# usar imagen sil pil, solo no se puede dimensionar

# imagen2 = Image.open('imagenes/favorite-1.jpg')
# imagen_redimensionada = imagen2.resize((70, 70))  #resize redimensiona imagen
# imagen_rotada = imagen_redimensionada.rotate(45)  # rotar imagen
# imagen_tk_2 = ImageTk.PhotoImage(imagen_redimensionada)

etiqueta = tk.Label(ventana, image= imagen_pil_2)
# boton = tk.Button(ventana, image=imagen_tk_2)

etiqueta.pack()
# boton.pack()

ventana.mainloop()
