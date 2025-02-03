# Video 45 trata de los cuadros de texto
# Temas
# - Input
# - Posicionamiento en en grillas
# - Posicionamiento de elementos dentro de las grillas (stiky)
# - Configuraciones en los input (show)

from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=350)
miFrame.pack()

miLabel = Label(miFrame, fg='blue', text='Mi Label:', font=('Comic Sans MS', 15))
miLabel.grid(row=1, column=1, sticky='w', pady=5, padx=5)

miCuadroTexto = Entry(miFrame, fg='red', font=('Comic Sans MS', 12))
miCuadroTexto.grid(row=2, column=1, pady=5, padx=5)



miLabelPassword = Label(miFrame, fg='blue', text='Mi Label Password:', font=('Comic Sans MS', 15))
miLabelPassword.grid(row=3, column=1, sticky='w', pady=5, padx=5)

miCuadroTextoPassword = Entry(miFrame, fg='red', font=('Comic Sans MS', 12))
miCuadroTextoPassword.grid(row=4, column=1, pady=5, padx=5)
miCuadroTextoPassword.config(show='$')


root.mainloop()