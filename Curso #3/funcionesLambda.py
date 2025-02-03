# Video 66 - Funciones Lambda: Sirve para simplicar funciones normales. 
# Su sentido es utilizarla para realizar acciones simples y rapidas.
# No se puede usar con funciones que sea muy complejas)

# Funcion Normal
def areaTriangulo(base, altura):
    return (base*altura)/2

print(areaTriangulo(4,8))

print('================================')

# Funcion Lamda o Anonima:
areaTrianguloLambda = lambda base,altura:(base*altura)/2

print(areaTrianguloLambda(6,9))
