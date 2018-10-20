"""
Enthält eine Klasse, die der Berechnung und Darstellung von Funktionen und deren Ableitungen dient.
Dazu wird die Methode der sogenannten Vorwärtsdifferenz verwendet.

A. Hnatiuk
M. Huneshagen
"""

import numpy as np
import matplotlib  
matplotlib.use("TkAgg") 
from matplotlib import pyplot as plt
import sys

class Plotten(object):
    def __init__(self, plotbereich, unten, oben, h, titel=""):
        """
        Initialisiert einen neuen Plot. 
        Dabei wird aus den Intervallgrenzen und der Länge der 
        Teilintervalle die Anzahl der Teilintervalle berechnet und 
        ein Array aus den Intervallgrenzen erstellt.
        """
        self.plotbereich = plotbereich
        self.unten = unten
        self.oben = oben
        self.h = h
        #self.fkt = fkt
        self.anz = int((oben - unten)/h) # Anzahl der Teilintervalle
        self.intervall = np.linspace(unten, oben, self.anz)
        self.plotbereich.set_title(titel)
        self.plotbereich.set_xlabel("$[a,b]$") 
        self.plotbereich.set_ylabel("$\mathbb{R}$")

    def plotfkt(self, fkt, name="Funktion"):
        self.plotbereich.plot(self.intervall, fkt(self.intervall), label=name)
        self.plotbereich.legend(loc="best")
    
    def plotablex(self, ablex, name="Erste Ableitung (exakt)"):
        self.plotbereich.plot(self.intervall, ablex(self.intervall), label=name)
        self.plotbereich.legend(loc="best")
    
    def plotabl2ex(self, abl2ex, name="Zweite Ableitung (exakt)"):
        self.plotbereich.plot(self.intervall, abl2ex(self.intervall), label=name)
        self.plotbereich.legend(loc="best")

    def plotabl(self, fkt, name="Erste Ableitung (appr.)"):
        abl = (fkt(self.intervall+self.h)-fkt(self.intervall))/self.h
        self.plotbereich.plot(self.intervall, abl, label=name)
        self.plotbereich.legend(loc="best")

    def plotabl2(self, fkt, name="Zweite Ableitung (appr.)"):
        abl2=(fkt(self.intervall+self.h) - 2*fkt(self.intervall) 
              + fkt(self.intervall-self.h))/self.h**2
        self.plotbereich.plot(self.intervall, abl2, label=name)
        self.plotbereich.legend(loc="best")


def negsin(x):
    """
    Diese Funktion besteht aus der zweiten Ableitung des Sinus, also -sin.
    """
    return -np.sin(x)


def test():
    """
    Testfunktion zum Testen der Plotten-Klasse. Es werden exakte und approximierte 
    Ableitungen geplottet. 
    Aufruf dieser Funktion erfolgt durch Übergabe von "test" beim Aufruf dieses Skripts
    """
    plt.figure(figsize=(20,10))
    
    # Plotten der appr. Funktionen im linken Subplot:
    
    AX_L = plt.subplot(121)
    IM_1 = Plotten(AX_L,0, 2*np.pi, 0.01)
    IM_1.plotfkt(np.sin)
    IM_1.plotabl(np.sin)
    IM_1.plotabl2(np.sin)

    # Plotten der exakten Funktionen im rechten Subplot:
    
    AX_R = plt.subplot(122)
    IM_2 = Plotten(AX_R, 0, 2*np.pi, 0.01)
    IM_2.plotfkt(np.sin)
    IM_2.plotablex(np.cos)
    IM_2.plotabl2ex(negsin)
    plt.show()

testing = False
for befehl in sys.argv:
    if befehl == "test":
        testing = True
        test()
if testing == False:
    print("Das Skript wird ohne Test beendet. Zum Testen der Funktionen übergeben Sie " + 
          "beim Aufruf \"test\"")






# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4



