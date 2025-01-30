# SIN POLIMORFISMO
class Carro():
    def desplazamiento(self):
        print('Desplazamiento en Cuatro Ruedas')


class Moto():
    def desplazamiento(self):
        print('Desplazamiento en Dos Ruedas')

class Camion():
    def desplazamiento(self):
        print('Desplazamiento en Seis Ruedas')


miCarro = Carro()
miCarro.desplazamiento()

miMoto = Moto()
miMoto.desplazamiento()

miCamion = Camion()
miCamion.desplazamiento()

print('==========================================')


# CON POLIMORFISMO
class Carro():
    def desplazamiento(self):
        print('Desplazamiento en Cuatro Ruedas')


class Moto():
    def desplazamiento(self):
        print('Desplazamiento en Dos Ruedas')

class Camion():
    def desplazamiento(self):
        print('Desplazamiento en Seis Ruedas')


miVeichulo = Camion()

def funcionPolimorfa(vehiculo):
    return vehiculo.desplazamiento()

funcionPolimorfa(miVeichulo)


