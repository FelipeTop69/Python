# Si no se entiende el principio de sustitucion ir al video 31 min 19.33 del curso

class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugar_residencia

    def descripcion(self):
        print('Descripcion Persona:' , '\nNombre:', self.nombre, '\nEdad:', self.edad, '\nLugar:', self.lugarResidencia)


personaUno = Persona('Felipe', '18', 'Colombia')
personaUno.descripcion()

print('==========================================')

class Empleado(Persona):

    # OJO QUE AQUI SE PASAN LOS ARGUMENTOS
    def __init__(self, salario, antiguedad, nombre, edad, lugar_residencia):

        # METODO ESPECIAL - Se pone el metodo super() seguido
        # del metodo al que se quiere acceder. En este caso el contructor
        super().__init__(nombre, edad, lugar_residencia)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()

        print('Salario:', self.salario, '\nAntiguedad:', self.antiguedad)



empleadoUno = Empleado(1200, 2, 'Samuel', 16, 'Colombia')
empleadoUno.descripcion()

print('==========================================')

# Principio de Sustiucion
print(isinstance(empleadoUno, Empleado))
print(isinstance(empleadoUno, Persona))

print('')

print(isinstance(personaUno, Empleado))
print(isinstance(personaUno, Persona))





