from tkinter import *

root = Tk()

miFrame = Frame(root)
miFrame.pack()
miFrame.config(bg='#757fe4')

# Para entender el funcionamiento de las funciones lambda ver el video 48 en el min 7:50

numeroPantalla = StringVar()
operacion = ''
resultado = 0

# Pantalla
pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg='black', fg='green', justify='right')

def capturarNumero(num):

    global operacion

    if (operacion != ''):
        numeroPantalla.set(num)
        operacion = ''
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


def suma(num):
    global operacion 
    global resultado

    resultado += int(num)

    operacion = 'suma'

    numeroPantalla.set(resultado)

def elResultado():
    global resultado

    numeroPantalla.set(resultado + int(numeroPantalla.get()))

    resultado = 0



# Fila uno Botones
botonNum7 = Button(miFrame, text='7', width=3, command=lambda:capturarNumero("7"))
botonNum7.grid(row=2, column=1)

botonNum8 = Button(miFrame, text='8', width=3, command=lambda:capturarNumero("8"))
botonNum8.grid(row=2, column=2)

botonNum9 = Button(miFrame, text='9', width=3, command=lambda:capturarNumero("9"))
botonNum9.grid(row=2, column=3)

botonDivi = Button(miFrame, text='/', width=3)
botonDivi.grid(row=2, column=4)

# Fila dos Botones
botonNum4 = Button(miFrame, text='4', width=3, command=lambda:capturarNumero("4"))
botonNum4.grid(row=3, column=1)

botonNum5 = Button(miFrame, text='5', width=3, command=lambda:capturarNumero("5"))
botonNum5.grid(row=3, column=2)

botonNum6 = Button(miFrame, text='6', width=3, command=lambda:capturarNumero("6"))
botonNum6.grid(row=3, column=3)

botonMul = Button(miFrame, text='x', width=3)
botonMul.grid(row=3, column=4)

# Fila tres Botones
botonNum1 = Button(miFrame, text='1', width=3, command=lambda:capturarNumero("1"))
botonNum1.grid(row=4, column=1)

botonNum2 = Button(miFrame, text='2', width=3, command=lambda:capturarNumero("2"))
botonNum2.grid(row=4, column=2)

botonNum3 = Button(miFrame, text='3', width=3, command=lambda:capturarNumero("3"))
botonNum3.grid(row=4, column=3)

botonRes = Button(miFrame, text='-', width=3)
botonRes.grid(row=4, column=4)

# Fila cuatro Botones
botonNum0 = Button(miFrame, text='0', width=3, command=lambda:capturarNumero("0"))
botonNum0.grid(row=5, column=1)

botonComa = Button(miFrame, text=',', width=3, command=lambda:capturarNumero(","))
botonComa.grid(row=5, column=2)

botonIgual = Button(miFrame, text='=', width=3, command=lambda:elResultado())
botonIgual.grid(row=5, column=3)

botonSum = Button(miFrame, text='+', width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)



root.mainloop()