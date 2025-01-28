#!/usr/bin/env python

# 4. La función directorio_padre devuelve el nombre del directorio que se encuentra 
# justo encima del directorio de trabajo actual. Recuerde que '..' es un alias de 
# ruta de acceso relativa que significa "subir al directorio principal". 
# Rellena los huecos para completar esta función.

import os

def parent_directory():
    # Create a relative path to the parent 
    # of the current working directory 
    relative_parent = os.path.join(os.getcwd(), '..')
    
    # Return the name of the parent directory
    return os.path.basename(os.path.abspath(relative_parent))

print(parent_directory())
