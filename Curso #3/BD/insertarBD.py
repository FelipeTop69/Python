import psycopg2 as pg

miConexion = pg.connect(
    dbname="bd_python",
    user="postgres",
    password="",
    host="localhost",
)
miConexion.autocommit = True  


miCursor = miConexion.cursor()

miCursor.execute('''

    INSERT INTO productos(nombre_producto, precio, seccion)
        VALUES ('Balon', 80000, 'Deportes');

''')

miCursor.close()
miConexion.close()
