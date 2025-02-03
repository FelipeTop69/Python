# Video 69
import re

cadena = 'Pinocho no sabia que era de madera, se hizo una paja y se prendio en candela'
print(re.search('madera', cadena))

palabraBuscar = 'pajaa'
busqueda = re.search(palabraBuscar, cadena)

print('============================================')

if(busqueda is not None):
    print('La palabra {} se encontro'.format(palabraBuscar))
else:
    print('La palabra {} no se encontro'.format(palabraBuscar))

print('============================================')


# Metodos del modulo

palabraBuscar = 'hizo'
busqueda = re.search(palabraBuscar, cadena)

# - Obtener la posicion inicial de la palabra
print('Posicion inicial:', busqueda.start())

# - Obtener la posicion final de la palabra
print('Posicion final:', busqueda.end())

# - Obtener ambas posiciones
print('Ambas posiciones:', busqueda.span())

# - Obtener todoas las coincidencias
busqueda = re.findall('se', cadena)
print('Todas las coincideenias:', busqueda)
print('Se encontraron', len(busqueda), 'coincidencias')