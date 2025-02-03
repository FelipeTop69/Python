# Video 46 trata de los cuadros de texto grandes y botones
# Temas en botones
# - Agregar botones
# - Agregar instrucciones a los botones
# - Establecer y obtener informacion
# - 

from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=350)
miFrame.pack()


miLabel = Label(miFrame, fg='blue', text='Mi Label:', font=('Comic Sans MS', 15))
miLabel.grid(row=1, column=1, sticky='w', pady=5, padx=5)

# Aqui se declara la varibale de esta forma debido a que mas abajo la estamos 
# estableciendo mediante una funcion con el metodo .set entonces este metodo 
# requiere este tipo de declaracion
miNombre = StringVar()
miCuadroTexto = Entry(miFrame, textvariable=miNombre, fg='red', font=('Comic Sans MS', 12))
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

def ponerNombre():
    miNombre.set('Felipe')

miBoton = Button(miFrame, text='Boton', command=ponerNombre)
miBoton.grid(row=7, column=1)


root.mainloop()