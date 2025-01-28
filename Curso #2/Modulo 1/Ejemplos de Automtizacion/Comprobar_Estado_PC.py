#!/usr/bin/env python
def comprobar_uso_disco(disco, umbral=20):
    infoDisco = shutil.disk_usage(disco)
    espacioLibre = infoDisco.free / infoDisco.total * 100
    return espacioLibre > umbral

def comprobar_uso_cpu(umbral=75):
    usoCPU = psutil.cpu_percent(1)
    return usoCPU < umbral

disco = "/"  # Cambiar a 'C:\\' en Windows
if not comprobar_uso_disco(disco) or not comprobar_uso_cpu():
    print("Error: Verifica el disco o el uso de CPU")
else:
    print("Todo está bien")

# Este script no funcionara porque no esta instalado el modulo de psutil