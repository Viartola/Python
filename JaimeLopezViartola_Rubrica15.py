#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import eyed3
import sqlite3
import datetime

eyed3.log.setLevel("ERROR")

con = sqlite3.connect("MP3_DB.db")
connCursor = con.cursor()

connCursor.execute("CREATE TABLE IF NOT EXISTS mp3 (title TEXT, artist TEXT, genre TEXT, duration CHAR(10))")


def showMenu():  
    os.system('clear')
    print "\n \033[94m", 60 * "/"
    print "\n \033[94m Bienvenido al gestor de canciones mp3, seleccione una opcion:"
    print ""
    print "\n \033[94m 1. Añadir una nueva cancion a la base de datos."
    print "\n \033[94m 2. Listar todos los generos musicales de la base de datos."
    print "\n \033[94m 3. Lisar todas las canciones de un interprete."
    print "\n \033[94m 4. Listar todas las canciones de un genero musical."
    print "\n \033[94m 5. Listar todas las canciones de la base de datos."
    print "\n \033[94m 6. Eliminar una cancion de la base de datos."
    print "\n \033[94m 7. Salir del gestor MP3."
    print ""
    print "\n", 60 * "/"
       
def mainLogic():
    showMenu()    
    userOption = int(raw_input("\n \033[94m Introduzca la opción a ejecutar: "))
    processOption(userOption) 
    
def comebackToMenu():
    raw_input("\n \033[93m Pulsa cualquier tecla para volver al menu del gestor MP3.")
    mainLogic()
    

def processOption(userOption): 
    if userOption == 1:
        showOption1()
    elif userOption == 2:
        showOption2()
    elif userOption == 3:
        showOption3()
    elif userOption == 4:
        showOption4()
    elif userOption == 5:
        showOption5()
    elif userOption == 6:
        showOption6()
    elif userOption == 7:
        showOption7()
    else :
        print"\n \033[91m ERROR - Elige una opcion de la lista."
        comebackToMenu();


    
def showOption1():
    os.system('clear')
    songPath = (raw_input("\n \033[94m Introduce una cancion de esta directorio (cancion.mp3) o escribe la ruta a una (/home/cancion.mp3): "))
    songFile = eyed3.load(songPath)
    
    con.execute("INSERT INTO mp3 (title, artist, genre, duration) VALUES ('" 
                 + str(songFile.tag.title) + "', '" 
                 + str(songFile.tag.artist) + "', '" 
                 + str(songFile.tag.genre.name) + "', '" 
                 + str(secs_to_MS(songFile.info.time_secs)) + "')")
    
    print "\033[92m   Titulo: " + str(songFile.tag.title)
    print "\033[92m   Interprete: " + str(songFile.tag.artist)
    print "\033[92m  Duracion: " + str(secs_to_MS(songFile.info.time_secs)) + "(" + str(songFile.info.time_secs) + " secs)"
    print "\033[92m  Genero: " + str(songFile.tag.genre.name)
    print ""
    con.commit()
    print "\033[94m La cancion ha sido insertada en la base de datos exitosamente.";
    
    comebackToMenu()
    
def secs_to_MS(secs):
    return datetime.datetime.fromtimestamp(secs).strftime('%M:%S') 
     
def showOption2():
    os.system('clear')
    print "\n \033[94m Listando todos los generos de la base de datos."
    connCursor = con.execute("SELECT title, artist, genre, duration FROM mp3 ORDER BY genre ASC")
    
    for row in connCursor:
        print "\033[92m   " + str(row[2]) 
    print " \033[94m Los generos han sido listados exitosamente."
    
    comebackToMenu()

def showOption3():
    os.system('clear')
    artistToFind = (raw_input("\n \033[94m Introduce un interprete: "))
    connCursor = con.execute("SELECT title, artist, genre, duration FROM mp3 WHERE artist='" 
                              + artistToFind + "' ORDER BY artist ASC")
    for row in connCursor:
        print "\033[92m  " + str(row[1]) + " - " + str(row[0]) +  " | " + str(row[2]) + " | " + str(row[3])
    print " \033[94m Se ha listado por el interprete: " + artistToFind + " exitosamente."
    
    comebackToMenu()

def showOption4():
    os.system('clear')
    genreToFind = (raw_input("\n \033[94m Introduce un genero: "))
    connCursor = con.execute("SELECT title, artist, genre, duration FROM mp3 WHERE genre='" 
                              + genreToFind + "' ORDER BY genre ASC")
    for row in connCursor:
        print "\033[92m  " + str(row[0]) + " - " + str(row[1]) + " | " + str(row[2])
    print " \033[94m Se ha listado por el genero: " + genreToFind + " exitosamente."
    
    comebackToMenu()
     
def showOption5():
    os.system('clear')
    print "\n \033[94m Listando todas las canciones de la base de datos."
    connCursor = con.execute("SELECT title FROM mp3 ORDER BY title ASC")
    for row in connCursor:
        print "\033[92m  " + str(row[0]) + "."
    print "\033[94m Se han listado todas las canciones exitosamente.";
    
    comebackToMenu()
    
def showOption6():  
    os.system('clear')
    titleToDelete = (raw_input("\n \033[94m Titulo de la cancion a eliminar: "))
    artistToDelete = (raw_input("\n \033[94m Interprete de la cancion a eliminar: "))
    connCursor = con.execute("DELETE FROM mp3 WHERE title='" + titleToDelete + "' AND artist='" + artistToDelete + "'")
    con.commit()
    print "\033[93m Se ha eliminado la cancion: " + titleToDelete + " - " + artistToDelete + " existosamente."
    comebackToMenu()

def showOption7():
    os.system('clear')
    print "\n \033[93m Saliendo del gestor MP3."
    con.close()
    quit()  
    
mainLogic()