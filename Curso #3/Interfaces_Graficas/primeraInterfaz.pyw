import tkinter



# Creacion de la raiz
raiz = tkinter.Tk()

# Titulo de la ventana o raiz
raiz.title('First Windows')

# Controlar la redimencion de la ventana por interaccion del usuario
    # - Se utilizan valores bool (True, False or 1,0)
    # - Se controla el ancho y alto
raiz.resizable(True,True)

#Cambiar Icono de la ventana
raiz.iconbitmap('./Icon/Icon.ico')

#Tamaño predeterminado de la ventana
raiz.geometry('720x540')

# Fondo
raiz.config(bg='#282622')

# Para evitar que la ejecutar el programa, la interfaz se abra 
# con la terminal hay que cambia la extension del archivo a .pyw

# Especie de blucle infinito que mantiene la raiz en vista (Reconmendable que vaya siempre al final)
raiz.mainloop()