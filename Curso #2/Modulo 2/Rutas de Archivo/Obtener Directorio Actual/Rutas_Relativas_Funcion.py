#!/usr/bin/env python
from pathlib import Path

# PASAR RUTAS DIRECTAMENTE COMO PARAMETROS
def crear_ruta_relativa(*subdirectorios, nombre_archivo=None):
    # Obtener el directorio actual
    directorio_actual = Path.cwd()
    
    # Construir la ruta con los subdirectorios
    ruta = directorio_actual.joinpath(*subdirectorios)
    
    # Si se proporciona un nombre de archivo, agregarlo a la ruta
    if nombre_archivo:
        ruta = ruta / nombre_archivo
    
    # Crear los directorios necesarios si no existen
    ruta.parent.mkdir(parents=True, exist_ok=True)
    
    return ruta

ruta_archivo = crear_ruta_relativa('Rutas de Archivo', 'Obtener Directorio Actual', nombre_archivo='Nombres02.txt')
print(f"Ruta generada: {ruta_archivo}")

ruta_directorio = crear_ruta_relativa('CarpetaPrincipal', 'Subcarpeta')
print(f"Ruta generada: {ruta_directorio}")


# PASAR UNA LISTA DERUTAS COMO PARAMETRO
def crear_ruta_relativa_lista(subdirectorios, nombre_archivo=None):

    # Obtener el directorio actual
    directorio_actual = Path.cwd()
    
    # Construir la ruta con los subdirectorios
    ruta = directorio_actual.joinpath(*subdirectorios)
    
    # Si se proporciona un nombre de archivo, agregarlo a la ruta
    if nombre_archivo:
        ruta = ruta / nombre_archivo
    
    # Crear los directorios necesarios si no existen
    ruta.parent.mkdir(parents=True, exist_ok=True)
    
    return ruta

subdirectorios01 = ['Rutas de Archivo', 'Obtener Directorio Actual']
ruta_archivo = crear_ruta_relativa_lista(subdirectorios01, nombre_archivo='Nombres02.txt')
print(f"Ruta generada: {ruta_archivo}")

subdirectorios02 = ['Proyectos', 'Python', 'Ejemplos']
ruta_directorio = crear_ruta_relativa_lista(subdirectorios02)
print(f"Ruta generada: {ruta_directorio}")

