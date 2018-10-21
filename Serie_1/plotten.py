"""
Enthaelt eine Klasse, die der Berechnung und Darstellung von Funktionen und deren Ableitungen dient.
Dazu wird die Methode der sogenannten Vorwaertsdifferenz verwendet.

A. Hnatiuk
M. Huneshagen
"""

import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import sys

class Plotten(object):
    """
    Diese Klasse erlaubt das Plotten von Funktionen und ihren Ableitungen (exakt und
    approximiert mit der Methode der Vorwaertsdifferenz).

    Attribute:

        plotbereich (pyplot.Axes-Objekt):
            Bestimmt, wohin die Funktionen gezeichnet werden.
        unten (float):
            Untere Intervallgrenze.
        oben (float):
            Obere intervallgrenze.
    """
    def __init__(self, plotbereich, unten, oben, titel=""):
        """
        Initialisiert einen neuen Plot.
        Die Achsen werden beschriftet, optional kann ein Plottitel uebergeben werden.

        Input:

            plotbereich (pyplot.Axes-Objekt):
                Bestimmt, wohin die Funktionen gezeichnet werden.
            unten (float):
                Untere Intervallgrenze.
            oben (float):
                Obere intervallgrenze.
            titel (str, optional, Standard:""):
                Titel des Plots.
        """
        self.plotbereich = plotbereich
        self.unten = unten
        self.oben = oben

        self.plotbereich.set_title(titel)
        self.plotbereich.set_xlabel(r"$[a,b]$")
        self.plotbereich.set_ylabel(r"$\mathbb{R}$")

    def intervall_h(self, h):
        """
        Erstellt ein ein Intervall mit vorgegebener Schrittweite h zwischen den
        Intervallgrenzen eines Plotten-Objekts. Ist die Intervalllaenge kein ganzzahliges
        Vielfaches von h, so wird die Anzahl der Teilintervalle kaufmaennisch gerundet.

        Input:

            h (float):
                Laenge der Teilintervalle

        Return:

            (numpy.ndarray) Array aus Teilintervallgrenzen.
        """
        anz_int = int((self.oben-self.unten)/h + 0.5) # Anzahl der Teilintervalle
        return np.linspace(self.unten, self.oben, anz_int)

    def plotfkt(self, fkt, name="Funktion"):
        """
        Plottet eine Funktion auf dem Intervall [a,b]. Das Intervall
        wird hierzu aequidistant in 1000 Teilintervalle eingeteilt, was eine
        gute Darstellung des Verlaufs gewaehrleistet.

        Input:

            fkt (function):
                Zu zeichnende Funktion.
            name (str, optional, Standard: "Funktion"):
                Legendeneintrag der zu zeichnenden Funktion.

        Return: -
        """
        intervall = np.linspace(self.unten, self.oben, 1001)
        self.plotbereich.plot(intervall, fkt(intervall), label=name)
        self.plotbereich.legend(loc="best")

    def plotablex(self, ablex, h=-1, name="Erste Ableitung (exakt)"):
        """
        Plottet eine Ableitungs-Funktion auf dem Intervall [a,b]. Das
        Intervall wird hierzu aequidistant in 1000 Teilintervalle eingeteilt,
        was eine gute Darstellung des Verlaufs gewaehrleistet.


        Input:

            ablex (function):
                Zu zeichnende Ableitungs-Funktion.
            name (str, optional, Standard: "Erste Ableitung (exakt)"):
                Legendeneintrag der zu zeichnenden Abl.-Funktion.

        Return: -
        """
        intervall = np.linspace(self.unten, self.oben, 1001)
        self.plotbereich.plot(intervall, ablex(intervall), label=name)
        self.plotbereich.legend(loc="best")

    def plotabl2ex(self, abl2ex, name="Zweite Ableitung (exakt)"):
        """
        Plottet eine zweite Ableitungs-Funktion auf dem Intervall [a,b]. Das
        Intervall wird hierzu aequidistant in 1000 Teilintervalle eingeteilt,
        was eine gute Darstellung des Verlaufs gewaehrleistet.


        Input:

            abl2ex (function):
                Zu zeichnende zweite Ableitungs-Funktion.
            name (str, optional, Standard: "Zweite Ableitung (exakt)"):
                Legendeneintrag der zu zeichnenden 2. Abl.-Funktion.

        Return: -
        """
        intervall = np.linspace(self.unten, self.oben, 1001)
        self.plotbereich.plot(intervall, abl2ex(intervall), label=name)
        self.plotbereich.legend(loc="best")

    def ablapprox(self, fkt, h):
        """
        Implementierung der Vorwaertsdifferenz.

        Input:
            fkt (function):
                Abzuleitende Funktion.
            h (float):
                Schrittweite der diskreten Differenziation.
        Return:
            (numpy.ndarray) mehrdimensionales Array:
                [x-Werte zwischen a und b, Werte von fkt' bei den x-Werten]
        """
        return np.array([self.intervall_h(h), (fkt(self.intervall_h(h)+h)
                                               - fkt(self.intervall_h(h)))/h])

    def abl2approx(self, fkt, h):
        """
        Implementierung des Differenzenquotients zur Approximation der zweiten Ableitung.

        Input:
            fkt (function):
                Abzuleitende Funktion.
            h (float):
                Schrittweite der diskreten Differenziation.

        Return:
            (numpy.ndarray) mehrdimensionales Array:
                [x-Werte zwischen a und b, Werte von fkt'' bei den x-Werten]

        """
        return np.array([self.intervall_h(h), (fkt(self.intervall_h(h)+h)
                                               - 2*fkt(self.intervall_h(h))
                                               + fkt(self.intervall_h(h)-h))/h**2])

    def plotabl(self, fkt, h, name="Erste Ableitung (appr.)"):
        """
        Plottet die per Vorwaertsdifferenz approximierte erste Ableitung einer
        gegebenen Funktion.

        Input:

            fkt (function):
                Abzuleitende Funktion.
            h (float):
                Schrittweite der diskreten Differenziation.
            name (str, optional, Standard:"Erste Ablleitung (appr.)"):
                Legendeneintrag der approx. Abl.-Funktion

        Return: -
        """
        x, y = self.ablapprox(fkt, h)
        self.plotbereich.plot(x, y, label=name)
        self.plotbereich.legend(loc="best")

    def plotabl2(self, fkt, h, name="Zweite Ableitung (appr.)"):
        """
        Plottet die per approximierte zweite Ableitung einer
        gegebenen Funktion.

        Input:

            fkt (function):
                Abzuleitende Funktion.
            h (float):
                Schrittweite der diskreten Differenziation.
            name (str, optional, Standard:"Erste Ablleitung (appr.)"):
                Legendeneintrag der approx. zweiten Abl.-Funktion

        Return: -
        """

        x, y = self.abl2approx(fkt, h)
        self.plotbereich.plot(x, y, label=name)
        self.plotbereich.legend(loc="best")

    def err_abl(self, fkt, h_arr, ablex):
        x, y = self.ablapprox(fkt,h_arr)
        error = np.abs(y - ablex(x))
        return(np.amax(error))

    def err_abl2(self, fkt, h_arr, ablex2):
        x, y = self.abl2approx(fkt,h_arr)
        error = np.abs(y - ablex2(x))
        return(np.amax(error))

def negsin(x):
    """
    Diese Funktion besteht aus der zweiten Ableitung des Sinus, also -sin.
    """
    return -np.sin(x)


def test():
    """
    Testfunktion zum Testen der Plotten-Klasse. Es werden exakte und approximierte
    Ableitungen geplottet.
    Aufruf dieser Funktion erfolgt durch Uebergabe von "test" beim Aufruf dieses Skripts
    """
    plt.figure(figsize=(20, 10))

    # zum Testen wird h=0.01 gesetzt:

    h_test = 0.01

    # Plotten der appr. Funktionen im linken Subplot:

    AX_L = plt.subplot(121)
    IM_1 = Plotten(AX_L, 0, 2*np.pi)
    IM_1.plotfkt(np.sin)
    IM_1.plotabl(np.sin, h_test)
    IM_1.plotabl2(np.sin, h_test)

    # Plotten der exakten Funktionen im rechten Subplot:

    AX_R = plt.subplot(122)
    IM_2 = Plotten(AX_R, 0, 2*np.pi)
    IM_2.plotfkt(np.sin)
    IM_2.plotablex(np.cos)
    IM_2.plotabl2ex(negsin)
    
    print(np.vectorize(IM_2.err_abl)(np.sin, np.array([h_test, 0.1]), np.cos))
    plt.show()


if __name__ == "__main__":
    testing = False
    for befehl in sys.argv:
        if befehl == "test":
            testing = True
            test()
    if testing == False:
        print("Das Skript wird ohne Test beendet. Zum Testen der Funktionen uebergeben Sie " +
              "beim Aufruf \"test\"")






# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
