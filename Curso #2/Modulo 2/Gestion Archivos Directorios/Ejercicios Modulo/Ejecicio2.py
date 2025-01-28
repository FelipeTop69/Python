#!/usr/bin/env python

# 2. La función nuevo_directorio crea un nuevo directorio dentro del directorio de trabajo actual, 
# luego crea un nuevo archivo vacío dentro del nuevo directorio, y devuelve la lista de archivos 
# en ese directorio. Rellena los huecos para crear un archivo "script.py" 
# en el directorio "PythonPrograms". 

import os

def new_directory(directory, filename):
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == False:
        os.mkdir(directory)

    # Create the new file inside of the new directory
    os.chdir(directory)
    with open (filename, 'w') as file:
        pass

    # Return the list of files in the new directory
    return os.listdir()

print(new_directory("PythonPrograms", "script.py"))