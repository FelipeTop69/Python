class Vehiculo():
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

class Vehiculo_Electrico(Vehiculo):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)

        self.autonomia = 100

    def carganado(self):
        self.carganado = True

# AQUI SE ESTA APLICANDO LA HERENCIA MULTIPLE
class Bicileta_Electrica(Vehiculo_Electrico, Vehiculo):
    pass

# En este caso al instanciar la clase que hereda de las otras dos clases 
# anteriores y ambas clases tienen constructor, solo heredara el constructor 
# de la clase que tenga prioridad, en este caso vendria siendo la clase Vehiculo_Electrico
# porque se pasa de primera en la herencia multiple. Asi mismo pasara con los metodos y atributos
miBici = Bicileta_Electrica('HERO', 'EXPULSE')



