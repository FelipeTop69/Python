from tkinter import *
from tkinter import messagebox as msg
import psycopg2 as pg

root = Tk()

# ----------BARRA MENU----------

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# Opcion BD
bdMenu = Menu(barraMenu, tearoff=0)
bdMenu.add_command(label='Conectar')
bdMenu.add_command(label='Salir')

# Opcion Limpiar Campso
limpiarCamposMenu = Menu(barraMenu, tearoff=0)
limpiarCamposMenu.add_command(label='Limpiar Campos')

# Opcion CRUD
crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label='Registrar')
crudMenu.add_command(label='Consultar')
crudMenu.add_command(label='Actualizar')
crudMenu.add_command(label='Borrar')

# Agregar opciones a la barra de menu
barraMenu.add_cascade(label='BD', menu=bdMenu)
barraMenu.add_cascade(label='Borrar', menu=limpiarCamposMenu)
barraMenu.add_cascade(label='CRUD', menu=crudMenu)

# ----------FIN BARRA MENU----------

# ----------CAMPOS CRUD----------

camposCrud = Frame(root)
camposCrud.pack()

# Campo ID
labelId = Label(camposCrud, text='Id: ', fg='blue', font=('Comic Sans MS', 10))
labelId.grid(row=0, column=0, padx=10)

campoId = Entry(camposCrud)
campoId.grid(row=0, column=1, pady=10)

# Campo Nombre
labelNombre = Label(camposCrud, text='Nombre: ', fg='blue', font=('Comic Sans MS', 10))
labelNombre.grid(row=1, column=0, padx=10)

campoNombre = Entry(camposCrud)
campoNombre.grid(row=1, column=1, pady=10)
campoNombre.config(fg='red')

# Campo Apellido
labelApellido = Label(camposCrud, text='Apellido: ', fg='blue', font=('Comic Sans MS', 10))
labelApellido.grid(row=2, column=0, padx=10)

campoApellido = Entry(camposCrud)
campoApellido.grid(row=2, column=1, pady=10)
campoApellido.config(fg='red')

# Campo Contraseña
labelContrasena = Label(camposCrud, text='Contraseña: ', fg='blue', font=('Comic Sans MS', 10))
labelContrasena.grid(row=3, column=0, padx=10)

campoCTS = Entry(camposCrud)
campoCTS.grid(row=3, column=1, pady=10)
campoCTS.config(show='§')

# Campo Comentario
labelComentario = Label(camposCrud, text='Comentarios: ', fg='blue', font=('Comic Sans MS', 10))
labelComentario.grid(row=4, column=0, padx=10)

textoComentario = Text(camposCrud, width=16, height=5)
textoComentario.grid(row=4, column=1, pady=10)

barraScroll = Scrollbar(camposCrud, command=textoComentario.yview)
barraScroll.grid(row=4, column=2, sticky='nsew')

textoComentario.config(yscrollcommand=barraScroll.set)

# ----------FIN CAMPOS CRUD----------

# ----------BOTONES CRUD----------

botonesCrud = Frame(root)
botonesCrud.pack()

# Boton Crear
btnCrear = Button(botonesCrud, text='Crear')
btnCrear.grid(row=1, column=0, sticky='e', padx=10, pady=10)
btnCrear.config(width=7, height=2)

# Boton Leer
btnLeer = Button(botonesCrud, text='Leer')
btnLeer.grid(row=1, column=1, sticky='e', padx=10, pady=10)
btnLeer.config(width=7, height=2)


# Boton Actualizar
btnActualizar = Button(botonesCrud, text='Actualizar')
btnActualizar.grid(row=1, column=2, sticky='e', padx=10, pady=10)
btnActualizar.config(width=8, height=2)


# Boton Borrar
btnBorrar = Button(botonesCrud, text='Borrar')
btnBorrar.grid(row=1, column=3, sticky='e', padx=10, pady=10)
btnBorrar.config(width=7, height=2)



# ----------FIN BOTONES CRUD----------





root.mainloop()
