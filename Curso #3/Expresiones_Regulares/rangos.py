# Video 71
import re as expRe

# Se nos permite buscar dentro de un rango de
listaNombres = ['Felipe', 'Samuel', 'Esteban', 'Daniel', 'Thaliana', 'Esteban'] 
for nombre in listaNombres:
    if expRe.findall('[p-t]', nombre):
        print(nombre)

print('=====================================')

# Tambien es posible negar el rango, es decir, que busque lo que no se encuentre dentro del rango
print('Ejemplo 01')
listaNombres = ['Ma1', 'Se1', 'Ma2', 'B1', 'M3', 'Va1', 'Va2', 'M4'] 
for nombre in listaNombres:
    if expRe.findall('M[^3-4]', nombre):
        print(nombre)

print('Ejemplo 02')
listaNombres = ['Ma1', 'Se1', 'Ma2', 'B1', 'Ma3', 'Va1', 'Va2', 'Ma4', 'MaA', 'MaB', 'Ma5', 'MaC'] 
for nombre in listaNombres:
    if expRe.findall('Ma[3-4A-B]', nombre):
        print(nombre)

print('=====================================')

# Busqueda que tenga o bien una cosa o la otra
listaNombres = ['Ma:1', 'Se1', 'Ma2', 'B.1', 'Ma3', 'Va1', 'Va:2', 'Ma4', 'Ma.A', 'MaB', 'Ma.5', 'MaC'] 
for nombre in listaNombres:
    if expRe.findall('[:.]', nombre):
        print(nombre)




