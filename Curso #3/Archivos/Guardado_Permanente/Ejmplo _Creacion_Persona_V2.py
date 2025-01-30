# Aqui ya estamos guardando y mostrando dichas personas de la lista en un fichero
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

    def __init__(self):

        achivoListaPersonas = open('listaPersonas', 'ab+')
        achivoListaPersonas.seek(0)

        try:
            self.personas = pickle.load(achivoListaPersonas)
            print('Se cargaron {} personas en el fichero externo'.format(len(self.personas)))
        except:
            print('El fichero esta vacio')
        finally:
            achivoListaPersonas.close()
            del achivoListaPersonas

    def guardarPersona(self, persona):
        self.personas.append(persona)
        self.guardarPersonaFichero()

    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)

    def guardarPersonaFichero(self):
        archivoListaPersonas = open('listaPersonas', 'ab+')
        pickle.dump(self.personas, archivoListaPersonas)
        archivoListaPersonas.close()
        del archivoListaPersonas

    def mostrarPersonasFichero(self):
        print('La informacion del fichero es la siguiente: ')
        for persona in self.personas:
            print(persona)



miLista = ListaPersonas()

persona1 = Persona('Felipe', 18, 'M')
miLista.guardarPersona(persona1)
miLista.mostrarPersonasFichero()

# miLista.guardarPersona(persona2)
# miLista.guardarPersona(persona3)

# miLista.mostrarPersonas()





