#!/usr/bin/env python
import os, datetime

print(os.path.getsize('Prueba.txt'))

marcaDeTiempo = os.path.getmtime("Prueba.txt")
print(datetime.datetime.fromtimestamp(marcaDeTiempo))

print(os.path.isfile('asd'))