#!/usr/bin/env python
print "*** buscador de palabras dentro de un archivo ***"
print "*************************************************"
print ""
fichero = raw_input("Inserte un fichero:")
palabra = raw_input("Inserte la palabra a buscar:")
fd = open(fichero)
lines = fd.readlines()
nlineas = 0
for linea in lines:
    palabras = linea.split(' ')
    for p in palabras:
        if p==palabra:             
            nlineas += 1
fd.close()
print "Numero de lineas que sale esa palabra:", nlineas