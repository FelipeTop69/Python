# Crear Clase
class Auto():
    largoChasis = 240
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos
        
        if self.enMarcha:
            return 'El auto esta en marcha'
        else:
            return 'El auto esta detenido'

    def estadoAuto(self):
        print('El largo de chasis es {} \n El ancho del chasis es {} \n Numero de Ruedas: {}'.format(self.largoChasis, self.anchoChasis, self.ruedas))

print('PRIMER OBJETO')
batiMovil = Auto()
print(batiMovil.arrancar(True))
batiMovil.estadoAuto()

print('==============================')

print('SEGUNDO OBJETO')
batiMovilDos = Auto()
print(batiMovilDos.arrancar(False))
batiMovilDos.estadoAuto()


