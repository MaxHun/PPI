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
from matplotlib.widgets import Slider, Button, RadioButtons


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
    h_arr = np.logspace(-17, 2, 5000)           #Werte der getesteten Schrittweiten
    p_werte = np.linspace(0, np.pi, 1000)
    sin_obj = differenzieren.Differenzieren(np.sin, np.cos, negsin, p_werte)
    j_slider = Slider(plt.axes([0.3, 0.01, 0.4, 0.03]), 'Waehlen Sie ein j:', 0.0,100 , valinit=1, valstep=0.0001) 
    j=2
    colors = ["r", "g", "b"]
    
    axis1.set_xlabel(r'Differenziationsschrittweite $h$')
    axis1.set_ylabel('Fehler der Ableitung')
    axis1.xaxis.set_label_coords(1.05, -0.055)
    
    axis2_neues_j = functools.partial(neues_j, plotbereich=axis2, slider=j_slider, p_werte=p_werte, h_arr=h_arr)
    j_slider.on_changed(axis2_neues_j)
    fehlerplot(axis1, sin_obj, h_arr)
    axis2.text(0.3,10**-12,"Wählen Sie  ein j mithilfe des Sliders unten")
    fig.legend(ncol=5, loc = (0.3,0.9), facecolor="w")
    fig.suptitle("Fehlerverhalten der Approximation der ersten und zweiten Ableitung")

    plt.subplots_adjust(wspace=0.0, top=0.94)
    plt.show()



def neues_j(val, slider, plotbereich, p_werte, h_arr):
    plotbereich.cla()
    j = slider.val
    plt.gcf().canvas.draw_idle()
    sin_j_fkt = functools.partial(sin_j,j=j)
    cos_j_fkt = functools.partial(cos_j,j=j)
    negsin_j_fkt = functools.partial(negsin_j,j=j)
    sin_j_obj = differenzieren.Differenzieren(sin_j_fkt, cos_j_fkt, negsin_j_fkt, p_werte)
    fehlerplot(plotbereich, sin_j_obj, h_arr, labeling=False)


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
