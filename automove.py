#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

dateien = []
zielverzeichniss = None
quellverzeichniss = None
dateiendung = "avi"
woerterbuch = {}
episoden = {}

def erstelleWoerterbuch():
    pass

def help():
    print "Dieses kleine Script kann Serien automatisch umbenennen und in ein bestimmtes Verzeichniss verschieben."
    print "Und so funktioniert es:"
    print "-f Datei -d Quellverzeichniss -z Zielverzeichniss"


##################################################
# Erstellen der Episodenliste , Schlagwortliste
def erstelleEpisoden():
    global episoden
    buch = open("episoden.txt", "r")
    for line in buch:
        line.strip()
        key, value = line.split()
        episoden.update({key : value })

##################################################
# Erstellen des Woerterbuchs, Schlagwortliste
def erstelleWoerterbuch():
    global woerterbuch
    buch = open("woerterbuch.txt", "r")
    for line in buch:
        line.strip()
        key, value = line.split()
        woerterbuch.update({key : value })

##################################################
# Ersetzt verschiedene Trenner durch einen Punkt
def getKeys(lastFile):
    lastFile = lastFile.replace("_",".")
    lastFile = lastFile.replace("/",".")
    lastFile = lastFile.replace("-",".")
    lastFile = lastFile.replace(" ",".")
    lastFile = lastFile.lower()
    # print lastFile # Debug-ausgabe
    Liste = lastFile.split(".")
    return Liste

##################################################
# identifizieren der Serie. Wie heißt die Serie?
def getSerienName(Liste):
    name = None
    for L in woerterbuch.keys():
        if L in Liste:
            name = woerterbuch[L]
             # print "Die Serie heist: ", name # Debug-Ausgabe
    return name

##################################################
# Welche Episode ist das?
def getEpisode(Liste):
    episode = None
    for L in episoden.keys():
        if L in Liste:
            episode = episoden[L]
            # print "Die Episode: ", episode # Debug-ausgabe
    return episode

##################################################
# Gib mir den Episoden Namen 
def getEpisodenName(serie, episode):
    seriedata = "./serien/" + serie + ".txt"
    # print "Dateiname: ", seriedata ' Debug-Ausgabe
    episodenname = None
    fobj = open(seriedata, "r")
    for line in fobj:
        line.strip()
        z = line.split()
        if z[0] ==  episode:
            episodenname = ".".join(z[1:])
            # print "Episodenname: ", episodenname #Debug-ausgabe
    fobj.close()
    return episodenname

##################################################
# Quellverzeichniss und Unterverzeichnisse einlesen
def getDateien(quelle):
    liste = []
    for e in os.listdir(quelle):
        if os.path.isfile(quelle + e):
            if e[-3:] == dateiendung:
                liste.append(quelle + e)
        if os.path.isdir(quelle + e):
            # print "-d- ", quelle + e # Debug-Ausgabe
            liste += getDateien(quelle + e + "/")
    return liste

##################################################
# verarbeiten der Schalter
def parameter():
    global zielverzeichniss
    global quellverzeichniss
    global dateien
    a = 1
    while a < len(sys.argv):
        if sys.argv[a] == "-f":
            a = a + 1
            dateien.append(sys.argv[a])
        elif sys.argv[a] == "-d":
            a += 1
            quellverzeichniss = sys.argv[a]
        elif sys.argv[a] == "-z":
            a += 1
            zielverzeichniss = sys.argv[a]
        else:
            print "Konnte Parameter ", sys.argv[a], "nicht einlesen"
            help()
            exit(1)
        a = a + 1
    
    if zielverzeichniss == None:
        print "Es wurde kein Zielverzeichniss angegeben"
        help()
        exit(1)


####################################################
##### Hauptprogramm ################################
####################################################

##### Vorbereitungen #######
parameter()
erstelleEpisoden()
erstelleWoerterbuch()

##### Einlesen des Quellverzeichnisses fals angegeben ####
if quellverzeichniss != None:
    print "Quellverzeichniss ", quellverzeichniss, " wird eingelesen"
    dateien += getDateien(quellverzeichniss)

##### Jetzt kanns endlich losgehen ########
nie = False
alle = False
for i in range(0,len(dateien)):
    Liste = getKeys(dateien[i])

    # Serie herausfinden
    serie = getSerienName(Liste)

    if serie == None:
        print "%100s   Serie unbekannt" % dateien[i]
        continue
    # Staffel und Episode herausfinden
    episode = getEpisode(Liste)
    if episode == None:
        print "%100s   Episode unbekannt" % dateien[i]
        continue

    episodenName = getEpisodenName(serie, episode)
    if episodenName == None:
        print "%100s   EpisodenName unbekannt" % dateien[i]
        continue
    nach = zielverzeichniss + ".".join([serie, episode, episodenName, Liste[-1]])
    print "%100s   %s" % (dateien[i], nach)

    if (not nie) and (not alle):
        verschieben = raw_input("Verschieben (Ja, Nein, Alle, Keine)? ")
        if verschieben == "K":
            nie = True
            verschieben = "N"
        elif verschieben == "A":
            alle = True
            verschieben = "J"
    if verschieben == "J":
        print "Verschiebe"
        os.rename(dateien[i], nach)
    else:
        print "Nicht Verschieben"
    


