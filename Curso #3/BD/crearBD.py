import psycopg2 as pg

# Conectar a la base de datos
miConexion = pg.connect(
    dbname="bd_python",
    user="postgres",
    password="",
    host="localhost",
)
miConexion.autocommit = True  # Permite que los cambios se guarden automáticamente

# Creacion del cursor para ejecutar sentencias SQL
miCursor = miConexion.cursor()

# Sentencia SQL
miCursor.execute('''

    CREATE TABLE productos(
        nombre_producto VARCHAR(50),
        precio INTEGER,
        seccion VARCHAR(20)
    )

''')


# Cerrar conexión
miCursor.close()
miConexion.close()
