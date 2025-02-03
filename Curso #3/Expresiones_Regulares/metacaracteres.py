# Video 70
import re as expRe

listaNombres = ['Felipe Tovar', 'Samuel Aviles', 'Esteban Correa', 'Daniel Aviles', 'Thaliana Quimbaya', 'Esteban Palomar']

# Uso de anclas
for nombre in listaNombres:
    # El simbolo '^' es una ancla y lo que hace es buscar el elemento que comienze por la cadena especificada
    if expRe.findall('^Esteban', nombre):
        print(nombre)

print('==================================')

for nombre in listaNombres:
    # El simbolo '$' es una ancla y lo que hace es buscar el elemento que termine por la cadena especificada
    if expRe.findall('Aviles$', nombre):
        print(nombre)

print('==================================')

# Uso clase de caracteres
print('Ejemplo 01')
# Dentro de '[]' podemos incluir cualquier carater sin importar el orden para buscar cadenas que lo contengan

listaDominios = ['felipeCaña.com', 'samuelArroz.es', 'estebanArbol.es', 'danielNiño.mx']
for dominio in listaDominios:
    if expRe.findall('[ñ]', dominio):
        print(dominio)

print('')

print('Ejemplo 02')
listaNombres = ['Hombre', 'Mujer', 'niño', 'niña']
for nombre in listaNombres:
    if expRe.findall('niñ[oa]', nombre):
        print(nombre)
