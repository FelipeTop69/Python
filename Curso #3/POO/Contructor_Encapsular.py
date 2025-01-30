# Crear Clase
class Auto():

    # Contructor
    def __init__(self):
        # Para encapsular se utiliza '__' y asi se seguirar 
        # utilizando dentro de constructor como por fuera
        # al encp
        self.__largoChasis = 240
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False


    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos
        
        if self.__enMarcha:
            return 'El auto esta en marcha'
        else:
            return 'El auto esta detenido'

    def estadoAuto(self):
        print('Largo chasis {} \n Ancho chasis {} \n Ruedas: {}'.format(self.__largoChasis, self.__anchoChasis, self.__ruedas))

print('PRIMER OBJETO')
batiMovil = Auto()

print(batiMovil.arrancar(True))
batiMovil.estadoAuto()

print('==============================')

print('SEGUNDO OBJETO')
batiMovilDos = Auto()

print(batiMovilDos.arrancar(False))
batiMovilDos.estadoAuto()

print('==============================')

print('TERCER OBJETO')
batiMovilTres = Auto()

print(batiMovilTres.arrancar(False))
# De esta manera ya no es posible acceder al a tributo debido a que
# esta encapsulado. Si es posible acceder dentro de la clase
batiMovilTres.ruedas = 4
batiMovilTres.estadoAuto()


