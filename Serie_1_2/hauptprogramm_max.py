"""
Dieses Programm dient zur Veranschaulichung der Fehler bei der Approximation der ersen und
zeweiten Ableitungen der Sinus Funtion durch die Methode der Vorwaertsdifferenz

A. Hnatiuk
M. Huneshagen
"""
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import differenzieren
from differenzieren import negsin
import functools


def sin_j(x, j=1):
    return np.sin(x*j)

def cos_j(x, j=1):
    return j*np.cos(x*j)

def negsin_j(x, j=1):
    return -j**2*np.sin(x*j)

def main():
    """
    In dieser Funktion werden das Differenzieren Objekt, das Array mit Schnittweitewerten und
    das Subplot erstellt, die danach zum Plotten der Verhaltung des Fehlers
    in Abhängigkeit der Schrittweite dienen.
    Input:-
    Return:-
    """
    h_test = 0.0001
    fig, [axis1, axis2] = plt.subplots(1, 2, figsize=(20, 10),sharey=True)
    h_arr = np.logspace(-10, 0, 100)           #Werte der getesteten Schrittweiten
    p_werte = np.linspace(0, np.pi, 1000)
    j=2
    sin_j_fkt = functools.partial(sin_j,j=j)
    cos_j_fkt = functools.partial(cos_j,j=j)
    negsin_j_fkt = functools.partial(negsin_j,j=j)

    sin_obj = differenzieren.Differenzieren(np.sin, np.cos, negsin, p_werte)
    sin_j_obj = differenzieren.Differenzieren(sin_j_fkt, cos_j_fkt, negsin_j_fkt, p_werte)
    #Hier werden die Funktion und ihre Ableitungen geplottet
    colors = ["r", "g", "b"]
    
    print("Der absolute Fehler in der ersten Ableitung" +
          " ist {0:.5f}".format(sin_obj.err_abl(h_test, grad=1))
          + ', Schrittweite {}'.format(h_test))
    print("Der absolute Fehler in der zweiten Ableitung" +
          " ist {0:.5f}".format(sin_obj.err_abl(h_test, grad=2))
          + ', Schrittweite {}'.format(h_test))
    fehlerplot(axis1, sin_obj, h_arr)
    fehlerplot(axis2, sin_j_obj, h_arr, labeling=False)

    axis1.set_xlabel(r'Differenziationsschrittweite $h$')
    axis1.set_ylabel('Fehler der Ableitung')
    axis1.xaxis.set_label_coords(1.05, -0.055)
    fig.legend(ncol=5, loc = (0.25,0.9))
    #fig.legend()
    fig.suptitle("Fehler")
    plt.subplots_adjust(wspace=0.0)
    plt.show()

def fehlerplot(plotbereich, diff_objct, h_arr, labeling=True):
    """
    In dieser Funktion wird ein Plot des relativen Fehlers
    in Abhängigkeit von der Schrittweite mittles der Differenzieren Klasse gezeichnet.
    Input:
        plotbereich (pyplot.Axes-Objekt):
            Subplot, auf dem das Plot erzeugt wird
        diff_objct (Differenzieren-Instanz):
            Differenzieren-Obejekt, das untersucht wird
        h_array (numpy.ndarray aus floats):
            Array mit den Schrittweiten

    Return:-
    """
    err_array1 = np.vectorize(diff_objct.err_abl)(h_arr, grad=1)   #Fehler 1. Ableitung
    err_array2 = np.vectorize(diff_objct.err_abl)(h_arr, grad=2)    #Fehler 2. Ableitung
    
    if labeling == True:
        mult = 1
    else:
        mult = 0

    plotbereich.loglog(h_arr, err_array1, 'g', label='Fehler in erster Ableitung'*mult)
    plotbereich.loglog(h_arr, err_array2, 'k', label='Fehler in zweiter Ableitung'*mult)
    plotbereich.loglog(h_arr, h_arr, 'g', ls="--", label=r'$y = h$'*mult)
    plotbereich.loglog(h_arr, (h_arr)**2, 'k', ls="--", label=r'$y = h^2$'*mult)
    plotbereich.loglog(h_arr, (h_arr)**3, 'b', ls="--", label=r'$y = h^3$'*mult)


if __name__ == "__main__":
    main()
