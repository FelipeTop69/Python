import psycopg2 as pg

miConexion = pg.connect(
    dbname="bd_python",
    user="postgres",
    password="",
    host="localhost",
)
miConexion.autocommit = True  


miCursor = miConexion.cursor()
miCursor.execute('SELECT * FROM productos')

variosProductos = miCursor.fetchall()

print(variosProductos)

print('==============================================')

for producto in variosProductos:
    print('Nombre Producto: {} - Precio: {}'.format(producto[0], producto[1]))



miCursor.close()
miConexion.close()
