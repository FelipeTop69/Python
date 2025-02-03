# En el video 44 minuto 1:20 nos muestra en una tabla las diferentes 
# algunas opciones que se le pueden mandar a un label}

from tkinter import *

root = Tk()
# Al pasarle root a clase Frame le estamos definiendo a que pertenecera 
# nuestro frame, en este  mi frame pertenecera al contenedor padre root
miFrame = Frame(root, width=500, height=350)
miFrame.pack()

# Label
miLabel = Label(miFrame, text='Hola Universo', fg='red', font=('Comic Sans MS', 20))
miLabel.place(x=240, y=120)

# Abrevitura de Label en caso de que no se vuelva a utilizar mas 
# la variable en el futuro, esto seria util para titulos
Label(miFrame, text='Hola Abreviatura').place(x=240, y=190)

root.mainloop()
