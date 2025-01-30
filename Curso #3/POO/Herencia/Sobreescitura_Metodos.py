class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca:', self.marca, '\nModelo:', self.modelo, '\nEn Marcha:', self.enMarcha, '\nFrenado:', self.frena)

class Moto(Vehiculo):
    caballito = ''

    def hacerCaballito(self):
        self.caballito = 'Esta activo el caballito'

    # Sobreescritura del metodo 'estado'
    def estado(self):
        print('Marca:', self.marca, '\nModelo:', self.modelo, '\nEn Marcha:', self.enMarcha, '\nFrenado:', self.frena, '\nCaballito:', self.caballito)

moto = Moto('KTM', 'DUKE 200')

moto.hacerCaballito()
moto.estado()

