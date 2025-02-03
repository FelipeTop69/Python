# Video 73 - Para entender mas ver el video (En resumidas cuentas es una funcion que retorna una funcion mejorada)

# Sintaxis basica
def funcionDecoradora(funcionADecorar):
    def funcionDecorada():
        print('Se va a realizar un calculo')

        funcionADecorar()

        print ('Se realizo el calculo')
    
    return funcionDecorada

# Funciones a decorar
@funcionDecoradora
def suma():
    print(6+9)

suma()

@funcionDecoradora
def resta():
    print(6-9)

resta()

print('==============================')

# Funciones sin decorar
def multiplicar():
    return (6*9)
print(multiplicar())

# Me di cuenta que al agregar return a la funcion que se va a decorar, esta no se ejecuta correctamente
