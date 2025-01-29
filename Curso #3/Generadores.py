# Un generador es un tipo de funcion la cual me va a crear un objeto iterable.
# Luego a este objeto iterable se le va agregando el valor de uno en uno cada vez que llame
# dicha funcion

# Ejemplo - Crear una lista de numeros pares

# FUNCION TRADICIONAL
def generarNumerosPares(limite):
    listaNumerosPares = []
    numeroPar = 1

    for iteracion in range(limite):
        listaNumerosPares.append(numeroPar * 2)
        numeroPar += 1


    return listaNumerosPares

print(generarNumerosPares(10))

print('===============================================' , end='\n')

# FUNCION GENERADORA
def numeroPares(limite):
    numeroPar = 1
    while numeroPar<=10:
        yield numeroPar*2
        numeroPar += 1

# Aqui creamos el objeto generador a partir de la funcion 
numeroPares = numeroPares(10)

# for numero in numeroPares:
#     print(numero , end=' ')

print('===============================================' , end='\n')

# Hasta aqui se esta haciendo casi lo mismo en las dos funcione.
# Pero ahora llamando la funcion de esta manera conseguiremos ver el 
# funcionamiento de las funciones generadoras

print(next(numeroPares))

print(next(numeroPares))

print(next(numeroPares))

print(next(numeroPares))

# Lo que esta pasando es que si se vuelve a tomar el valor de esta funcion no devolvera 
# todo el objeto sino que por cada llamada creara el valor nuevo y lo devolvera

print('===============================================' , end='\n')


# FUNCION GENERADORA CON NUEVA UTILIDA PARA SIMPLIFICAR 
# CODIGO EN CASO DEL USO DE  BUCLES ANIDADOS

# Pre Ejercicio para entender

# El '*' seguido del parametro indica que se pasaran una cantidad 
# desconocida de argumeros y seran almacenados como tupla
def devuelveCiudades(*ciudades):
    for ciudad in ciudades:
        yield ciudad

# Creamos el objetos generador
listaCiudades = devuelveCiudades('Neiva', 'Pereira', 'Barranquilla', 'Bogoto', 'Medellin')

print(next(listaCiudades))
print(next(listaCiudades))

print('===============================================' , end='\n')

# Bucle For Anidado a partir del Ejemplo

def devuelveCiudadesAnidado(*ciudades):
    for ciudad in ciudades:
        for letraCiudad in ciudad:
            yield letraCiudad

# Creamos el objetos generador
listaCiudadesAnidados = devuelveCiudadesAnidado('Neiva', 'Pereira', 'Barranquilla', 'Bogoto', 'Medellin')

print(next(listaCiudadesAnidados))
print(next(listaCiudadesAnidados))


print('===============================================' , end='\n')

# Aqui utilizaremos la utilidad 
def devuelveCiudadesAnidadoUtilidad(*ciudades):
    for ciudad in ciudades:
            yield from ciudad

# Creamos el objetos generador
listaCiudadesAnidadosUtilidad = devuelveCiudadesAnidadoUtilidad('Neiva', 'Pereira', 'Barranquilla', 'Bogoto', 'Medellin')

print(next(listaCiudadesAnidadosUtilidad))
print(next(listaCiudadesAnidadosUtilidad))






