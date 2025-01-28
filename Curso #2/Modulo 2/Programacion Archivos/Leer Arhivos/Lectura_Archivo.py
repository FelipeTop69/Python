#!/usr/bin/env python
file = open("./Curso #2/Modulo 2/Programacion Archivos/Leer Arhivos/Lectura.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()

with open('./Curso #2/Modulo 2/Programacion Archivos/Leer Arhivos/Lectura.txt') as file:
    print(file.readline())

with open('./Curso #2/Modulo 2/Programacion Archivos/Leer Arhivos/Lectura.txt') as file:
    for line in file:
        print(line.strip().upper())

with open('./Curso #2/Modulo 2/Programacion Archivos/Leer Arhivos/Lectura.txt') as file:
    lines = file.readlines()
    lines.sort()

print(lines)



