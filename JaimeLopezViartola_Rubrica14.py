#!/usr/bin/env python
""" Determina el numero de lineas de 'datos_ficheros' """
fichero = raw_input("Inserte un fichero:")
palabra = raw_input("Inserte la palabra a buscar:")
fd = open(fichero, "r")
nlineas = 0
for linea in fd:             
    nlineas += 1
fd.close()
print "Numero de lineas que sale esa palabra:", nlineas