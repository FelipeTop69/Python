#!/usr/bin/env python
msgErrorAccion = 'Error: Accion no valida'
msgErrorNumero = 'Error: Tipo de numero no valido'
mgsError = "Error: Ingrese un valor valido"

# -- PARA ENTEROS
def obtenerNumero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            if numero.is_integer():
                return numero
            else:
                print(msgErrorNumero)
        except ValueError:
            print(mgsError)

# -- PARA DECIMALES
# def obtenerNumero(mensaje):
#     while True:
#         try:
#             return float(input(mensaje))
#         except ValueError:
#             print(mgsError)

numeroUno = obtenerNumero("Ingrese el primer numero: ")
numeroDos = obtenerNumero("Ingrese el segundo numero: ")

operacionRealizar = 0

while operacionRealizar != 6:
    print("")
    print("Indique la operacion a realiar: ")
    print("")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Cambio de Valores")
    print("6) Salir")
    print("")


    try:
        operacionRealizar = int(input("Opcion: "))

        if operacionRealizar == 1:
            print("")
            suma = numeroUno + numeroDos
            resultado = "Suma {:.0f} + {:.0f} = {:.0f}".format(numeroUno, numeroDos, suma)  
            print(resultado)
        elif operacionRealizar == 2:
            print("")
            resta = numeroUno - numeroDos
            resultado = "Resta {:.0f} - {:.0f} = {:.0f}".format(numeroUno, numeroDos, resta)  
            print(resultado)
        elif operacionRealizar == 3:
            print("")
            multiplicacion = numeroUno * numeroDos
            resultado = "Multiplicacion {:.0f} * {:.0f} = {:.0f}".format(numeroUno, numeroDos, multiplicacion)  
            print(resultado)
        elif operacionRealizar == 4:
            print("")
            if numeroDos == 0:
                print("Error: No se puede dividir por 0")
            else:
                division = numeroUno / numeroDos
                resultado = "Division {:.0f} / {:.0f} = {:.2f}".format(numeroUno, numeroDos, division)  
                print(resultado)
        elif operacionRealizar == 5:
            print("")
            numeroUno = int(input("Ingrese el primer numero: "))
            numeroDos = int(input("Ingrese el segundo numero: "))
        elif operacionRealizar == 6:
            print("Saliendo...")
        else:
            print(msgErrorAccion)
    except ValueError:
        print(mgsError)
