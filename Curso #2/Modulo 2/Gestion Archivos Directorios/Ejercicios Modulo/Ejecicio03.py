#!/usr/bin/env python

# 3. La función fecha_archivo crea un nuevo archivo en el directorio de trabajo actual, 
# comprueba la fecha en que se modificó el archivo y devuelve sólo la parte de fecha de 
# la marca de tiempo en el formato aaaa-mm-dd. Rellene los campos para crear un archivo 
# llamado "archivo_nuevo.txt" y compruebe la fecha en que se modificó.

import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w'):
        pass
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    # Return just the date portion 
    # Hint: how many characters are in “yyyy-mm-dd”? 
    return ("{date}".format(date = date))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd