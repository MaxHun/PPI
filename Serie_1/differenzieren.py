"""
Enthaelt eine Klasse, die der Berechnung und Darstellung von Funktionen und deren Ableitungen dient.
Dazu wird die Methode der sogenannten Vorwaertsdifferenz für die erste Ableitung verwendet.

Arsen Hnatiuk
Max Huneshagen
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

class Differenzieren(object):
    """
    Diese Klasse erlaubt das Plotten von Funktionen und ihren Ableitungen (exakt und
    approximiert).

    Attribute:

        ablex_lis (list):
            Liste aus den ersten drei (anfangend bei 0) exakten Ableitungen der
            zu untersuchenden Funktion. Der list-Index gibt hierbei den Grad der
            Ableitung an, wobei die Funktion selbst als nullte Ableitung aufgefasst wird.
        p_arr (numpy.ndarray aus floats):
            Plotpunkte, an denen die Funktionen geplottet bzw. für die Fehlerbestimmung aus-
            gewertet werden.
    """
    def __init__(self, fkt, abl_ex, abl2_ex, p_arr):
        """
        Initialisiert ein neues Differenzieren-Objekt. Legt aus der gegebenen Funktion und deren
        Ableitungen eine Liste an.

        Input:

            fkt (function):
                Bestimmt, wohin die Funktionen gezeichnet werden.
            abl_ex (function):
                Exakte erste Ableitung.
            abl2_ex (function):
                Exakte zweite Ableitung.
            p_arr (numpy.ndarray aus floats):
                Plotpunkte, an denen die Funktionen geplottet bzw. für die Fehlerbestimmung aus-
                gewertet werden.

        Return: -
        """
        self.ablex_lis = [fkt, abl_ex, abl2_ex] # Liste aus exakten Ableitungen
        self.p_arr = p_arr

    def plotfkt_exakt(self, plotbereich, grad=0, **kwargs):
        """
        Plottet eine ("exakte") Funktion an den Plotpunkten in einen zu übergebenden Plot.
        Man kann zwischen nullter, erster und zweiter Ableitung waehlen.

        Input:

            plotbereich (pyplot.Axes-Objekt):
                Bestimmt, wohin die Funktion geplottet wird.
            grad (int, optional, Standard: 0):
                Grad der Ableitung. Bei grad==0 wird die Funktion selbst geplottet.
            **kwargs (keyword arguments, optional):
                Keyword arguments zur Uebergabe an pyplot.plot. Nachzulesen in der
                matplotlib.lines.Line2D-Doku.

        Return: -
        """
        plotbereich.plot(self.p_arr, self.ablex_lis[grad](self.p_arr), **kwargs)

    def ablapprox(self, schrittw, grad=1):
        """
        Diese Funktion approximiert die erste oder zweite Ableitung der Funktion
        an den plotpunkten. Wird als Grad der zu approximierenden Ableitung 0
        angegeben, so wird der Funktionswert an der Plotpunkten zurückgegeben.

        Input:

            schwrittw (float):
                Schrittweite der diskreten Differenziation.
            grad (int, optional, Standard: 1):
                Grad der gewuenschten Ableitung. bei grad==0 werden die Funktionswerte
                an den Plotpunkten zurückgegeben.
        Return:
            (numpy.ndarray aus floats):
                [Werte der <grad>ten Ableitung der Funktion an den Plotpunkten]
        """
        fkt = self.ablex_lis[0]

        if grad == 0:
            return fkt(self.p_arr)
        elif grad == 1:
            return (fkt(self.p_arr+schrittw)- fkt(self.p_arr))/schrittw
        elif grad == 2:
            return (fkt(self.p_arr+schrittw) - 2*fkt(self.p_arr)
                    + fkt(self.p_arr-schrittw))/schrittw**2

        # Falls als Grad ein ungültiger Ausdruck eingegeben wird, wird der Nutzer darauf
        # hingewiesen:schrittw

        print("Die Funktion ablapprox kann nur die erste oder die zweite Ableitung " +
              "berechnen, bitte geben Sie als Grad 1 oder 2 ein (Standard: 1)")

    def plotfkt_approx(self, schrittw, plotbereich, grad=1, **kwargs):
        """
        Plottet die approximierte Ableitung (eines bestimmten Grades) der Funktion.
        Dabei wird die Funktion als nullte Ableitung aufgefasst.

        Input:

            schwrittw (float):
                Schrittweite der diskreten Differenziation.
            plotbereich (pyplot.Axes-Objekt):
                Bestimmt, wohin die Funktion geplottet wird.
            grad (int, optional, Standard: 1):
                Grad der gewünschten Ableitung. Bei grad==0 wird die Funktion selbst geplottet.
            **kwargs (keyword arguments, optional):
                Keyword arguments zur Uebergabe an pyplot.plot. Nachzulesen in der
                matplotlib.lines.Line2D-Doku.

        Return: -
        """
        y_werte = self.ablapprox(schrittw, grad=grad)
        plotbereich.plot(self.p_arr, y_werte, **kwargs)

    def err_abl(self, schrittw, grad=1):
        """
        Diese Funktion bestimmt das Maximum der absoluten Differenz zwischen approximierter
        Ableitung einer Funktion und der exakten Ableitung an den Plotpunkten.

        Input:

            schwrittw (float):
                Schrittweite der diskreten Differenziation.
            grad (int, optional, Standard: 1):
                Grad der gewuenschten Ableitung. bei grad==0 wird als Fehler 0 zurueckgegeben,
                da die Funktion selbst exakt gegeben ist.

        Return:
            (float) Maximale absolute Abweichung der approximierten Ableitung von ablex.
        """
        abl_werte = self.ablapprox(schrittw, grad=grad)
        error = np.abs(abl_werte - self.ablex_lis[grad](self.p_arr))
        return np.amax(error)

def negsin(arg):
    """
    Diese Funktion besteht aus der zweiten Ableitung des Sinus, also -sin.

    Input:

            arg (float):
                Stelle, die untersucht werden soll.

    Return:
            (float) Wert von -sin an der Stelle arg.
    """
    return -np.sin(arg)


def test():
    """
    Testfunktion zum Testen der Plotten-Klasse. Es werden exakte und approximierte
    Ableitungen geplottet.
    Aufruf dieser Funktion erfolgt durch Uebergabe von "test" beim Aufruf dieses Skripts
    """
    h_test = 0.01                                               # zum Testen wird h=0.01 gesetzt
    p_werte = np.linspace(0, np.pi, 1000)                       # Plotpunkte
    sin_diff = Differenzieren(np.sin, np.cos, negsin, p_werte)  # Neues Objekt initialisieren
    fig, [ax_l, ax_r] = plt.subplots(1, 2, figsize=(20, 10))

    # Exakte Funktionen werden links geplottet:

    for grad in [0, 1, 2]:
        sin_diff.plotfkt_exakt(ax_l, grad=grad, label="{}. Ableitung (exakt)".format(grad))
    # Die exakte Funktion und die approx. Ableitungen werden rechts geplottet:

    for grad in [0, 1, 2]:
        sin_diff.plotfkt_approx(h_test, ax_r, grad=grad,
                                label="{}. Ableitung (approx.)".format(grad))

    for axis in [ax_l, ax_r]:
        axis.set_xlim(0, np.pi)
        axis.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
        axis.set_xticklabels(["$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$",
                              r"$\pi$"])
        axis.legend(loc="upper right")
        axis.set_xlabel('Definitionsbereich der Abbildung')
        axis.set_ylabel('Werte der Abbildung')
    fig.suptitle("Test der Funktionalität der Klasse anhand der Sinus-Funktion")
    plt.show()


if __name__ == "__main__":
    # Uebergibt man beim Aufruf den String "test", so wird als Test der Sinus und seine ersten
    # beiden Ableitungen (exakt und approximiert) geplottet. Ansonsten wird lediglich ein Hinweis
    # darauf der Standardausgabe uebergeben.
    TESTING = False
    for befehl in sys.argv:
        if befehl == "test":
            TESTING = True
            test()
    if not TESTING:
        print("Das Skript wird ohne Test beendet. Zum Testen der Funktionen uebergeben Sie " +
              "beim Aufruf \"test\"")
