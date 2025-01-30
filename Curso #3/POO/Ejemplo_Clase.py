# Crear Clase
class Auto:
    # Atributos
    largoChasis = 240
    anchoChasis = 120
    ruedas = 4
    enMarcha = False

    # Metodos
    def arrancar(self):
        # Esto de abajito es como si estuvieramos diciendo 'batiMovil.enMarcha = True'
        self.enMarcha = True

    def estadoAuto(self):
        if self.enMarcha:
            return 'El auto esta en marcha'
        else:
            return 'El auto esta detenido'
    

# Instanciar clase que al tiempo viene siendo la creacion de nuestro objeto
batiMovil = Auto() #Creamos el objeto auto

# Acceder a los atributos de mi objeto
print('El largo del chasis es' + str(batiMovil.largoChasis))
print('El ancho del chasis es' + str(batiMovil.anchoChasis))

# Utilizar metodo de mi objeto
batiMovil.arrancar()

print(batiMovil.estadoAuto())