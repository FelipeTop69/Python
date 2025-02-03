# Video 46 trata de los cuadros de texto grandes y botones
# Temas en cuadro de texto big
# - Configuracion de las dimensiones en 
# - Crear scrollbar, agregarla a un elemento y configurar esta barra (adaptacion de tamaño y comportamiento de la barra desplazamaiento)

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



miLabelTextBIf = Label(miFrame, fg='blue', text='Comentarios:', font=('Comic Sans MS', 15))
miLabelTextBIf.grid(row=5, column=1, sticky='w', pady=5, padx=5)

miCuadroTextoBig = Text(miFrame, fg='red', font=('Comic Sans MS', 12),  width=16, height=5)
miCuadroTextoBig.grid(row=6, column=1, pady=5, padx=5)

barraScroll = Scrollbar(miFrame, command=miCuadroTextoBig.yview)
barraScroll.grid(row=6, column=2, sticky='snew')

miCuadroTextoBig.config(yscrollcommand=barraScroll.set)



root.mainloop()