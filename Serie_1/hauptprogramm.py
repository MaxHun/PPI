"""
Dieses Programm dient zur Veranschulichung der Fehler bei der Approcimation der ersen und
zeweiten Ableitungen der Sinus Funtion durch die Methode der Vorwaertsdifferenz

A. Hnatiuk
M. Huneshagen
"""
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import plotten
from plotten import negsin

def fktn(wert):
    """
    Das ist die zweite Ableitung der Testfunktion
    Input:
        wert (float):
            Wert, auf dem man die Funktion evaliuiren will
    Return: -
    """
    return -np.sin(wert)

def main():
    """
    In dieser Funktion werden das Plotten Objekt, das Array mit Schnittweitewerten und
    das Subplot erstellt, die danach zum Plotten der Verhaltung des Fehlers
    in Abhängigkeit der Schrittweite dienen.
    Input:-
    Return:-
    """
    plt.figure(figsize=(20, 10))
    axis = plt.subplot(121)
    h_array = np.logspace(-4, 0, 100)             #Werte der getesteten Schrittweiten
    objct = plotten.Plotten(axis, 0, np.pi)
    #Hier werden die Funktion und ihre Ableitungen geplottet
    axis2 = plt.subplot(122)
    objct2 = plotten.Plotten(axis2, 0, np.pi)
    objct2.plotfkt(1000, np.sin)
    objct2.plotabl(np.sin, (2*np.pi)/1000)
    objct2.plotabl2(np.sin, (2*np.pi)/1000)
    objct2.plotablex(1000, np.cos)
    objct2.plotabl2ex(1000, negsin)
    axis2.set_title('Die Funktion und ihre Ableitungen (exacte und approximierte)')
    print("Der absolute Fehler in der ersten Ableitung" +
          " ist {0:.5f}".format(objct2.err_abl(np.cos, (2*np.pi)/1000, negsin)))
    print("Der absolute Fehler in der zweiten Ableitung" +
          " ist {0:.5f}".format(objct2.err_abl2(np.cos, (2*np.pi)/1000, negsin)))
    method(axis, objct, h_array)

def method(axis, objct, h_array):
    """
    In dieser Funktion wird ein Plot des relativen Fehlers
    in Abhängigkeit von der Schrittweite mittles der Plotten Klasse gezeichnet.
    Input:
        axis (axes-Objekt): Subplot, auf dem das Plot erzeugt wird
        objct (Plotten): Das Plotten Obkekt, auf dem der Fehler berechnet wird
        h_array (numpy.ndarray): Array mit den Schnittweitewerten
    Return:-
    """
    err_array1 = np.vectorize(objct.err_abl)(np.sin, h_array, np.cos)   #Fehlern 1. Ableitung
    err_array2 = np.vectorize(objct.err_abl2)(np.sin, h_array, fktn)    #Fehlern 2. Ableitung
    axis.loglog(h_array, err_array1, 'g', label='Fehler in erster Ableitung')
    axis.loglog(h_array, err_array2, 'k', label='Fehler in zweiter Ableitung')
    axis.loglog(h_array, h_array, 'g', ls="--", label=r'$y = h$')
    axis.loglog(h_array, (h_array)**2, 'k', ls="--", label=r'$y = h^2$')
    axis.loglog(h_array, (h_array)**3, 'b', ls="--", label=r'$y = h^3$')

    axis.set_title('Absoluter Fehler in Abhängigkeit von der Schrittweite')
    axis.set_xlabel(r'Schrittweite $h$')
    axis.set_ylabel('Relativer Fehler')
    axis.legend()
    plt.show()

if __name__ == "__main__":
    main()
