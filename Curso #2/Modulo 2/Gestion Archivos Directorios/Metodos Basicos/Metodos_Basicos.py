#!/usr/bin/env python
import os

os.remove('PruebaBorrar.txt')

os.rename('Rename01.txt', 'Rename02.txt')

existencia = os.path.exists("Rename01.txt")
if existencia:
    print('Existe')
else:
    print('No Existe')