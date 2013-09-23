#!/usr/bin/python
# -*- coding: utf-8 -*-


#### Script zum erstellen der Episodenliste ###
import sys

s = 30
e = 30
a = 1
while a < len(sys.argv):
    if sys.argv[a] == "-s":
        a = a + 1
        s = sys.argv[a]
    elif sys.argv[a] == "-e":
        a += 1
        e = sys.argv[a]
    elif sys.argv[a] == "-h":
        print "mögliche Parameter:"
        print " -s Anzahl Staffeln (default = 3)"
        print " -e Anzal Episoden (default = 3)"
        exit(1)
    else:
        print "Konnte Parameter ", sys.argv[a], "nicht einlesen"
        exit(1)
    a = a + 1


for i in range(1,s):
    for j in range(1,e):
        print "s%02de%02d   S%02dE%02d" % (i, j, i, j)
for i in range(1,2):
    for j in range(1,e):
        print "%dx%02d  S%02dE%02d" % (i, j, i, j)
