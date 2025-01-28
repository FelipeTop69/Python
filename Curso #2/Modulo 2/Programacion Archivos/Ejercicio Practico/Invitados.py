#!/usr/bin/env python

# CREAR EL ARCHIVO CON LA LISTA DE INVITADOS
listaPersonas = ['Felipe', 'Samuel', 'Daniel', 'Esteban']

with open('./Curso #2/Modulo 2/Programacion Archivos/Ejercicio Practico/Lista_Invitados.txt', 'w') as lista:
    for persona in listaPersonas:
        lista.write(persona + '\n')

with open('./Curso #2/Modulo 2/Programacion Archivos/Ejercicio Practico/Lista_Invitados.txt') as lista:
    for personaInvitada in lista:
        print(personaInvitada.strip())

# ------------------------------------------------------------------

# AGREGAR NUEVOS INVITADOS AL ARCHIVO
nuevasPersonas = ['Bianchi', 'Juan David', 'Bata']

with open('./Curso #2/Modulo 2/Programacion Archivos/Ejercicio Practico/Lista_Invitados.txt', 'a') as lista:
    for personaNueva in nuevasPersonas:
        lista.write(personaNueva + '\n')

with open('./Curso #2/Modulo 2/Programacion Archivos/Ejercicio Practico/Lista_Invitados.txt') as lista:
    for personaInvitada in lista:
        print(personaInvitada.strip())

# ------------------------------------------------------------------

# SACAR INVITADOS DEL ARCHIVO
invitadosFuera = ['Felipe', 'Esteban', 'Juan David']
listaInvitadosTemporal = []

with open('./Curso #2/Modulo 2/Programacion Archivos/Ejercicio Practico/Lista_Invitados.txt') as lista:
    for invitado in lista:
        listaInvitadosTemporal.append(invitado.strip())

with open('./Curso #2/Modulo 2/Programacion Archivos/Ejercicio Practico/Lista_Invitados.txt', 'w') as lista:
    for invitado in listaInvitadosTemporal:
        if invitado not in invitadosFuera:
            lista.write(invitado + '\n')

# ------------------------------------------------------------------

# REVISAR INVITADOS EN LA LISTA
invitadosRevisar = ['Felipe', 'Bianchi']

with open('./Curso #2/Modulo 2/Programacion Archivos/Ejercicio Practico/Lista_Invitados.txt') as lista:
    listaInvitadosRevisar = [invitado.strip() for invitado in lista]

for invitadoRevisar in invitadosRevisar:
    if invitadoRevisar in listaInvitadosRevisar:
        print('{} esta en la lista'.format(invitadoRevisar))
    else:
        print('{} no esta en la lista'.format(invitadoRevisar))






