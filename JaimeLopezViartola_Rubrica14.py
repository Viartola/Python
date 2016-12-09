#!/usr/bin/env python
print "*************************************************"
print "*** Buscador de palabras dentro de un archivo ***"
print "*************************************************"
file = raw_input("Inserte un fichero:")
fd = open(file)
lines = fd.readlines()
word = raw_input("Inserte la palabra a buscar:")
nlines = 0
for line in lines:
    words = line.split()
    for w in words:
       if w == word:             
           nlines += 1
fd.close()
print "Numero de lineas que sale esa palabra:", nlines