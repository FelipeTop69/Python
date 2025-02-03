from tkinter import *

# Para ver las posibles configuraciones ir al video 43 del curso en el min 2:08

raiz = Tk()

raiz.title('First Frame')

raiz.resizable(True,True)

raiz.iconbitmap('./Icon/Icon.ico')

# raiz.geometry('720x540')

raiz.config(bg='#282622')

# Creacion de Frame 

# Hasta el momento el frame esta creado pero no se vera reflejado 
# porque no se a posicionado en la raiz o no se ha empaquetado
miFrame=Frame()

# Aqui ya se emaqueto en la raiz y se esta configurando
# En el mismo video en el min 7:04 muestra distinas configuraciones al empaquetar un frame
# Recomendable verlo todo para ver la distintas dimensiones que se le pueden dar
miFrame.pack()

miFrame.config(bg='orange')

miFrame.config(width='720', height='540', cursor='pirate')


raiz.mainloop()