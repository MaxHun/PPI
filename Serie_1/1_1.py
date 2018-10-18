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


class Plotten(object):
    def __init__(self, plotbereich, oben, unten, h):
        """
        Initialisiert einen neuen Plot. 
        Dabei wird aus den Intervallgrenzen und der Länge der 
        Teilintervalle die Anzahl der Teilintervalle berechnet und 
        ein Array aus den Intervallgrenzen erstellt.
        """
        self.plotbereich = plotbereich
        self.oben = oben
        self.unten = unten
        self.h = h
        #self.fkt = fkt
        self.anz = int((oben - unten)/h) # Anzahl der Teilintervalle
        self.intervall = np.linspace(unten, oben, self.anz)
    def plotfkt(self, fkt):
        self.plotbereich.plot(self.intervall, fkt(self.intervall))
    
  

plt.figure()
AX=plt.subplot(111)
IM_1 = Plotten(AX, 2*np.pi, 0, 0.01)
IM_1.plotfkt(np.sin)


plt.show()







# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4



