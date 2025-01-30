# En este primer punto simplemente estamos guardando y leyendo personas en una lista
import pickle

class Persona():

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        print('Se ha creado una nueva persona con el nombre:', self.nombre)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.edad, self.genero)

class ListaPersonas():

    personas = []

    def guardarPersona(self, persona):
        self.personas.append(persona)

    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)


persona1 = Persona('Samuel', 16, 'M')
persona2 = Persona('Saray', 19, 'F')
persona3 = Persona('Felipe', 18, 'M')

miLista = ListaPersonas()

miLista.guardarPersona(persona1)
miLista.guardarPersona(persona2)
miLista.guardarPersona(persona3)

miLista.mostrarPersonas()


