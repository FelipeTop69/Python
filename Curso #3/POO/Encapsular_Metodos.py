# Crear Clase
class Auto():

    def __init__(self):
        self.__largoChasis = 240
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False


    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if self.__enMarcha:
            chequeo = self.__chequeoInterno()

        if self.__enMarcha and chequeo:
            return 'El coche esta en marcha'
        elif self.__enMarcha and chequeo == False:
            return 'Problema en el chequeo'
        else:
            return 'El coche esta detenido'



    def estadoAuto(self):
        print('Largo chasis {} \n Ancho chasis {} \n Ruedas: {}'.format(self.__largoChasis, self.__anchoChasis, self.__ruedas))

    def __chequeoInterno(self):
        self.combustible = 'ok'
        self.acite = 'ok'
        self.puertas = 'cerradas'

        print('Iniciando Chequeo')

        if self.combustible == 'ok' and self.acite == 'ok' and self.puertas == 'cerradas':
            return True
        else:
            return False


print('PRIMER OBJETO')
batiMovil = Auto()

print(batiMovil.arrancar(True))
batiMovil.estadoAuto()

print('==============================')

print('SEGUNDO OBJETO')
batiMovilDos = Auto()

print(batiMovilDos.arrancar(False))
batiMovilDos.estadoAuto()






