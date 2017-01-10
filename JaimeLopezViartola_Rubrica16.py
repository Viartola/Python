#!/usr/bin/env python
#-*- coding: utf-8 -*-
from datetime import datetime
import math
import os

print "*********************************"
print "*** Calculadora de Biorritmos ***"
print "*********************************"
print " "

name = raw_input("Introduzca su nombre: ")
date = raw_input("Introduzca su fecha de nacimiento (dd/mm/yyyy): ")
birthday = datetime.strptime(date, '%d/%m/%Y')
	
numberDays = (datetime.utcnow() - birthday).days

if numberDays<0:
    print "Fecha Incorrecta"
    exit()  

x = 2*math.pi*numberDays
physical = round(math.sin(x/23)*100)
emotional = round(math.sin(x/28)*100)
intellectual = round(math.sin(x/33)*100)

os.system('clear')

print "El pronostico de tus Biorritmos", name, "es:"
print "Fisico: ", physical,"%"
print "Emocional: ", emotional,"%"
print "Intelectual: ", intellectual,"%"