#!/usr/bin/env python
import os

# Crear un diccionario vacío
outputs = {}

# Guardar el directorio actual en el diccionario
outputs['directorio_actual'] = os.getcwd()

# Cambiar a otro directorio
os.chdir("..")  # Ir al directorio padre
outputs['directorio_padre'] = os.getcwd()

# Regresar al directorio inicial
os.chdir(outputs['directorio_actual'])
outputs['regreso_directorio_actual'] = os.getcwd()

# Mostrar todas las rutas guardadas
for key, value in outputs.items():
    print(f"{key}: {value}")
