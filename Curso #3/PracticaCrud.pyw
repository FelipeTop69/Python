from tkinter import *
from tkinter import messagebox as msg
import psycopg2 as pg
from psycopg2 import errors  # Importar errores específicos

# ----------FUNCIONALIDAD----------
# ---------------------------------

# Funcion Conexion BD
def conexionBD():
    try:
        miConexion = pg.connect(
            dbname="bd_python_crud",
            user="postgres",
            password="",
            host="localhost"
        )

        miConexion.autocommit = True
        miCursor = miConexion.cursor()

        miCursor.execute("""
            CREATE TABLE usuarios(
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(50),
                apellido VARCHAR(50),
                password VARCHAR(50),
                comentarios TEXT
            )
        """)

        msg.showinfo('Bases de Datos', 'Se conecto exitosamente con la base de datos.')
    
    except errors.DuplicateTable:
        msg.showwarning('Bases de Datos', 'La base de datos ya existe.')
    except Exception as e:
        msg.showerror('Error', f'Ocurrió un error: {e}')
    finally:
        miCursor.close()
        miConexion.close()


# Funcion limpiar campos
def limpiarCampos():
    miId.set('')
    miNombre.set('')
    miApellido.set('')
    miContrasena.set('')
    textoComentario.delete(1.0, END)

# ----------OPCIONES CRUD----------

# Opcion Crear
def crear():

    nombre = miNombre.get()
    apellido = miApellido.get()
    contrasena = miContrasena.get()
    texto = textoComentario.get(1.0, END)

    miConexion = pg.connect(
        dbname="bd_python_crud",
        user="postgres",
        password="",
        host="localhost"
    )
    miConexion.autocommit = True  


    miCursor = miConexion.cursor()

    miCursor.execute('''

        INSERT INTO usuarios(nombre, apellido, password, comentarios)
            VALUES (%s, %s, %s, %s);

    ''', (nombre, apellido, contrasena, texto))

    # OJO - Al pasar parametros en una tupla hay q pasarlos como tupla o lista, no de forma inidivual

    miCursor.close()
    miConexion.close()

    limpiarCampos()

    msg.showinfo('Base de Datos', 'Insertado con exito')


# Opcion Leer
def leer():

    Id = miId.get()

    try:
        Id = int(Id)
    except ValueError:
        msg.showwarning('Base de Datos', 'Ingrese un valor valido')
        return

    miConexion = pg.connect(
        dbname="bd_python_crud",
        user="postgres",
        password="",
        host="localhost"
    )
    miConexion.autocommit = True  


    miCursor = miConexion.cursor()

    miCursor.execute('''

        SELECT * FROM usuarios WHERE id = %s

    ''', (Id,))
    # OJO - Cuando se pasa un solo valor como tupla es necesario poner una como al final para que esta sea intepreada como tupla

    datosUsuarios = miCursor.fetchall()

    if datosUsuarios:
        for datoUsuario in datosUsuarios:
            miId.set(datoUsuario[0])
            miNombre.set(datoUsuario[1])
            miApellido.set(datoUsuario[2])
            miContrasena.set(datoUsuario[3])
            textoComentario.insert(1.0, datoUsuario[4])
    else:
        msg.showwarning('Bases de Datos', 'No existe el usuario')
        limpiarCampos()

    miCursor.close()
    miConexion.close()

# Opcion Actualizar
def actualizar():

    iD = miId.get()
    nombre = miNombre.get()
    apellido = miApellido.get()
    contrasena = miContrasena.get()
    texto = textoComentario.get(1.0, END)

    miConexion = pg.connect(
        dbname="bd_python_crud",
        user="postgres",
        password="",
        host="localhost"
    )
    miConexion.autocommit = True  


    miCursor = miConexion.cursor()

    miCursor.execute('''

        UPDATE usuarios
        SET nombre=%s, apellido=%s, password=%s, comentarios=%s
        WHERE id = %s;

    ''', (nombre, apellido, contrasena, texto, iD))

    miCursor.close()
    miConexion.close()

    limpiarCampos()

    msg.showinfo('Base de Datos', 'Actualizado con exito')

# Opcion borrar
def borrar():

    Id = miId.get()

    try:
        Id = int(Id)
    except ValueError:
        msg.showwarning('Base de Datos', 'Ingrese un valor valido')
        return


    miConexion = pg.connect(
        dbname="bd_python_crud",
        user="postgres",
        password="",
        host="localhost"
    )
    miConexion.autocommit = True  


    miCursor = miConexion.cursor()

    try:
        miCursor.execute('''
            DELETE FROM usuarios
            WHERE id = %s;
        ''', (Id,))

        if miCursor.rowcount == 0:
            msg.showwarning('Bases de Datos', 'El usuario a borrar no existe')
        else:
            msg.showinfo('Base de Datos', 'Borrado con éxito')  

    except psycopg2.Error as e:
        msg.showwarning('Bases de Datos', f'Error al intentar borrar el usuario: {e}')
    finally:
        miCursor.close()
        miConexion.close()
        limpiarCampos()


    



# ----------INTERFAZ----------
# ----------------------------
root = Tk()

# ----------BARRA MENU----------

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

# Opcion BD
bdMenu = Menu(barraMenu, tearoff=0)
bdMenu.add_command(label='Conectar', command=conexionBD)
bdMenu.add_command(label='Salir', command=root.quit)

# Opcion Limpiar Camp0
limpiarCamposMenu = Menu(barraMenu, tearoff=0)
limpiarCamposMenu.add_command(label='Limpiar Campos', command=limpiarCampos)

# Opcion CRUD
crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label='Registrar', command=crear)
crudMenu.add_command(label='Consultar', command=leer)
crudMenu.add_command(label='Actualizar', command=actualizar)
crudMenu.add_command(label='Borrar', command=borrar)

# Agregar opciones a la barra de menu
barraMenu.add_cascade(label='BD', menu=bdMenu)
barraMenu.add_cascade(label='Borrar', menu=limpiarCamposMenu)
barraMenu.add_cascade(label='CRUD', menu=crudMenu)

# ----------FIN BARRA MENU----------

# ----------CAMPOS CRUD----------

camposCrud = Frame(root)
camposCrud.pack()

# Variables de campos
# Al campo Comentario no es necesario declararlo porque no es un entry
miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miContrasena = StringVar()

# Campo ID
labelId = Label(camposCrud, text='Id: ', fg='blue', font=('Comic Sans MS', 10))
labelId.grid(row=0, column=0, padx=10)

campoId = Entry(camposCrud, textvariable=miId)
campoId.grid(row=0, column=1, pady=10)

# Campo Nombre
labelNombre = Label(camposCrud, text='Nombre: ', fg='blue', font=('Comic Sans MS', 10))
labelNombre.grid(row=1, column=0, padx=10)

campoNombre = Entry(camposCrud, textvariable=miNombre)
campoNombre.grid(row=1, column=1, pady=10)
campoNombre.config(fg='red')

# Campo Apellido
labelApellido = Label(camposCrud, text='Apellido: ', fg='blue', font=('Comic Sans MS', 10))
labelApellido.grid(row=2, column=0, padx=10)

campoApellido = Entry(camposCrud, textvariable=miApellido)
campoApellido.grid(row=2, column=1, pady=10)
campoApellido.config(fg='red')

# Campo Contraseña
labelContrasena = Label(camposCrud, text='Contraseña: ', fg='blue', font=('Comic Sans MS', 10))
labelContrasena.grid(row=3, column=0, padx=10)

campoCTS = Entry(camposCrud, textvariable=miContrasena)
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
btnCrear = Button(botonesCrud, text='Crear', command=crear)
btnCrear.grid(row=1, column=0, sticky='e', padx=10, pady=10)
btnCrear.config(width=7, height=2)

# Boton Leer
btnLeer = Button(botonesCrud, text='Leer', command=leer)
btnLeer.grid(row=1, column=1, sticky='e', padx=10, pady=10)
btnLeer.config(width=7, height=2)


# Boton Actualizar
btnActualizar = Button(botonesCrud, text='Actualizar', command=actualizar)
btnActualizar.grid(row=1, column=2, sticky='e', padx=10, pady=10)
btnActualizar.config(width=8, height=2)


# Boton Borrar
btnBorrar = Button(botonesCrud, text='Borrar', command=borrar)
btnBorrar.grid(row=1, column=3, sticky='e', padx=10, pady=10)
btnBorrar.config(width=7, height=2)

# ----------FIN BOTONES CRUD----------

root.mainloop()
