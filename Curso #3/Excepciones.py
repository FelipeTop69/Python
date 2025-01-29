import math
# Controlador de Exepciones - Una excepcion es un error que ocurre durante la ejecucion del codigo

# Ejemplo 1 - Excepciones Individuales

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'No se puede entre 0'

# while True:
#     try:
#         num1 = int(input('Primer Numero:'))
#         num2 = int(input('Segundo Numero:'))
#         break
#     except ValueError:
#         print('Valor no valido, itente de nuevo')


print('''Operaciones 
    Suma
    Resta
    Multiplicacion
    Division
''')

# op = input('Escribe operacion: ').lower().strip()

# if op == 'suma':
#     print(suma(num1, num2))
# elif op == 'resta':
#     print(resta(num1, num2))
# elif op == 'multiplicacion':
#     print(multiplicacion(num1, num2))
# elif op == 'division':
#     print(division(num1, num2))
# else:
#     print('Operacion no Valida')


print('===============================================' , end='\n')

# Ejemplo 2 - Expeciones Multiples

def dividir():
    try:
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))

        print('Resultado' + str(num1 / num2))
    except ValueError:
        print('Numero no valido')
    except ZeroDivisionError:
        print('No se puede dividir por cero')

# dividir()

print('===============================================' , end='\n')

# Ejemplo 3 - Expeciones General

def dividirDos():
    try:
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))

        print('Resultado' + str(num1 / num2))
    except:
        print('Ha ocurrido un error')

# dividirDos()

print('===============================================' , end='\n')

# Ejemplo 4 - Expecion con Finally (Lo que este dentro de finally se ejecutara si o si)

def dividirTres():
    try:
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))

        print('Resultado' + str(num1 / num2))
    except:
        print('Ha ocurrido un error')
    finally:
        print('Calculo Terminado')

# dividirTres


print('===============================================' , end='\n')

# Ejemplo 5 - Lanzar Excepciones Provocadas 

def evluarEdad(edad):
    if edad < 0:
        raise ValueError('Edad no valida')
    elif edad < 20:
        return ('Eres muy Joven')
    elif edad < 40:
        return ('Eres Joven')
    elif edad < 65:
        return ('Eres maduro')
    elif edad < 100:
        return ('Cuidate...')


# print(evluarEdad(50))

print('===============================================' , end='\n')


# Ejemplo 6 - Controlar Excepcione Provocadas

def raizNumero(numero):

    if numero < 0:
        raise ValueError('Los negativos no tienen raiz cuadrada')
    else:
        return math.sqrt(numero)


numero = float(input('Numero: '))

try:
    print(raizNumero(numero))
except ValueError as numeroNegativo:
    print(numeroNegativo)





