import psycopg2 as pg

miConexion = pg.connect(
    dbname="bd_python",
    user="postgres",
    password="",
    host="localhost",
)
miConexion.autocommit = True 

miCursor = miConexion.cursor()

variosProductos = [
    ('Camiseta', 90000, 'Deportes'),
    ('Jarron', 50000, 'Hogar'),
    ('Lego Mercedez F1', 106000, 'Toys'),
]

# Sentencia SQL - Se utiliza el executemany para poder pasar varios registros como lista 
# # Esto '%s' se le conoce como marcadores de posicion, cambiaran segun el gestor
miCursor.executemany('''
    INSERT INTO productos(nombre_producto, precio, seccion)
        VALUES (%s, %s, %s)
''', variosProductos)


miCursor.close()
miConexion.close()
