#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
print "*************************************************"
print "*** Buscador de palabras dentro de un archivo ***"
print "*************************************************"


def search():  
    vector.append(word)
    f = open(file)
    lines = f.readlines()
    for line in lines:
            words = line.split(' ')
            for p in words:
                      for x in range(len(vector) ):
                             if p == vector[x]:
                                      print(line)                      
                                     
def insert():
    word = raw_input("Inserte una nueva palabra a buscar: ")
    search()
    delete()
    question()


def question():
    question = raw_input("Quieres añadir nueva palabra [s/n]: ")
    if question == "si" or question == "SI" or question == "S" or question == "s":
         insert()
    elif question == "no" or question == "NO" or question == "N" or question == "n" :
        print "************************"
        print "*** Hasta la proxima ***"
        print "************************"
        sys.exit(0)
    else:
        print "**********************************"
        print "*** Inserte un caracter valido ***"
        print "**********************************"
        question2()

def question2():
    question = raw_input("Quieres añadir nueva palabra [s/n]: ")
    if question == "si" or question == "SI" or question == "S" or question == "s":
         insert()
    elif question == "no" or question == "NO" or question == "N" or question == "n" :
        print "************************"
        print "*** Hasta la proxima ***"
        print "************************"
        sys.exit(0)
    else:
        print "**********************************"
        print "*** Inserte un caracter valido ***"
        print "**********************************"
        question()
        
def delete():
    vector.remove(word)
               
file = raw_input("Inserte un fichero: ")
word = raw_input("Inserte la palabra a buscar: ")
vector = [ ]
search()
delete()
question()