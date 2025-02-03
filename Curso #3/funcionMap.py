# Video 67 - Funcion Map: Nos devuelve un objeto en el que se 
# encuentran ciertos elementos que han sido generados con una funcion

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

# Esta funcion se la pasamos a map y es donde esta el sentido de la funcionalidad map
def comisionEmpleado(empleado):
    empleado.salarioo = empleado.salarioo * 1.03
    return empleado

listaEmpleadosComision = map(comisionEmpleado, listaEmpleados)

for empleadoComision in listaEmpleadosComision:
    print(empleadoComision)





