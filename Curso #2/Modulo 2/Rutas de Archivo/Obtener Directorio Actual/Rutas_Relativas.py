#!/usr/bin/env python
import os
from pathlib import Path

# METODO SENCILLO

listaNombres = ['Felipe', 'Samuel', 'Julian Esteban', 'Daniel', 'Bianchi']

# Crear la ruta relativa usando os.getcwd()
directorio_actual = os.getcwd()
ruta_archivo = os.path.join(directorio_actual, 'Rutas de Archivo', 'Obtener Directorio Actual', 'Nombres01.txt')

# Asegura que el archivo exista. Si el archivo junto con los directorios no existen entonces los crea, si existen no pada nasa
os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

# Escribir en el archivo
with open(ruta_archivo, 'w') as file:
    for nombre in listaNombres:
        file.write(nombre + '\n')

print(f"Archivo creado en: {ruta_archivo}")

# ============================================================================
# ============================================================================

# METODO MODERN0

listaNombres02 = ['Felipe02', 'Samuel02', 'Julian Esteban02', 'Daniel02', 'Bianchi02']

# Crear una ruta con pathlib
directorio_actual02 = Path.cwd()
ruta_archivo02 = directorio_actual02 / 'Rutas de Archivo' / 'Obtener Directorio Actual' / 'Nombres02.txt'

# Asegura que el archivo exista. Si el archivo junto con los directorios no existen entonces los crea, si existen no pada nasa
ruta_archivo02.parent.mkdir(parents=True, exist_ok=True)

# Escribir en el archivo
with open(ruta_archivo02, 'w') as file:
    for nombre in listaNombres02:
        file.write(nombre + '\n')

print(f"Archivo creado en: {ruta_archivo02}")
