# Video 67 - Funcion Filter: Nos devuelve un objeto en el que se 
# encuentran ciertos elementos que han cumplido con una condicion 

def numeroPar(num):
    if num % 2 == 0:
        return True

numeros = [1,2,3,4,5,6,7,8,9,10,11,12]

print(filter(numeroPar, numeros))

print('')

# Para poder ver, debemos convertirlo en una lista
print(list(filter(numeroPar, numeros)))

print('=====================================')

# Simplificando la funcion
resultado = filter(lambda numeros:numeros % 2 == 0, numeros)
print(list(resultado))

print('=====================================')

# Ejemplo Complejo pasando objetos y no listas

class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salarioo = salario

    def __str__(self):
        return '{} que trabaja de {} tiene un salario de {}'.format(self.nombre, self.cargo, self.salarioo)


listaEmpleados = [

    Empleado('Samuel', 'Ing Electronico', 8500),
    Empleado('Esteban', 'Ing Ambiental', 9000),
    Empleado('Daniel', 'Ing Aeronautico', 10000),
    Empleado('Felipe', 'Ing Softwarw', 10000),
    Empleado('Thaliana', 'Medio', 8100),

]

sueldoMayor = filter(lambda empleado:empleado.salarioo > 7000, listaEmpleados)

for empleado in sueldoMayor:
    print(empleado)


