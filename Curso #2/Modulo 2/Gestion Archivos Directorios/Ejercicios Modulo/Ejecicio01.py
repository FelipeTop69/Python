#!/usr/bin/env python

# 1. La función create_python_script crea un nuevo script de Python en el directorio 
# de trabajo actual, le añade la línea de comentarios declarada por la variable 'comments' 
# y devuelve el tamaño del nuevo archivo. Rellena los huecos para crear un script 
# llamado "programa.py".

import os
def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, 'w') as file:
        file.write(comments)
    filesize = os.path.getsize(filename)
    return(filesize)

print(create_python_script("program.py"))