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

def main():
    """
    In dieser Funktion werden das Differenzieren Objekt, das Array mit Schnittweitewerten und
    das Subplot erstellt, die danach zum Plotten der Verhaltung des Fehlers
    in Abhängigkeit der Schrittweite dienen.
    Input:-
    Return:-
    """
    abbr = 1           #Abbruchindex
    while abbr == 1:    #In dieser Schleife wird die Schrittweite durch den Benutzer ermittelt
        try:
            h_test = np.pi/float(input('Mit welcher Schrittweite pi/n wollen Sie die Ableitungen' +
                                 ' approximieren?\n' +
                                 'Schreiben Sie bitte eine echt positive Zahl n, z.B. 1\n'))
            abbr = 0
        except ValueError:
            print('Nicht gültiger Wert eingegeben. Versuchen Sie erneut.')
            abbr = 1
        if h_test <= 0:
            print('Nicht gültiger Wert eingegeben. Versuchen Sie erneut.')
            abbr = 1
    [axis1, axis2] = plt.subplots(1, 2, figsize=(20, 10))[1]
    h_arr = np.logspace(-2, 2, 100)           #Werte der getesteten Schrittweiten
    p_werte = np.linspace(0, np.pi, 1000)
    sin_obj = differenzieren.Differenzieren(np.sin, np.cos, negsin, p_werte)
    #Hier werden die Funktion und ihre Ableitungen geplottet
    colors = ["r", "g", "b"]
    sin_obj.plotfkt_exakt(axis2, color="m", label=r"$\sin(x)$")
    for grad in [1, 2]:
        sin_obj.plotfkt_exakt(axis2, grad=grad, color=colors[grad-1], alpha=0.3,
                              lw=4, label="{}. Ableitung, exakt".format(grad))
        sin_obj.plotfkt_approx(h_test, axis2, grad=grad, color=colors[grad-1],
                               ls="--", label="{}. Ableitung, approximiert".format(grad))
    axis2.set_title('Die Funktion und ihre Ableitungen (exakte und approximierte mit'+
                    ' Schrittweite {}'.format(h_test)+ ')')
    print("Der absolute Fehler in der ersten Ableitung" +
          " ist {0:.5f}".format(sin_obj.err_abl(h_test, grad=1))
          + ', Schrittweite {}'.format(h_test))
    print("Der absolute Fehler in der zweiten Ableitung" +
          " ist {0:.5f}".format(sin_obj.err_abl(h_test, grad=2))
          + ', Schrittweite {}'.format(h_test))
    fehlerplot(axis1, sin_obj, h_arr)
    axis1.legend()
    axis2.set_xlim(0, np.pi)
    axis2.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
    axis2.set_xticklabels(["$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$", r"$\frac{3\pi}{4}$",
                           r"$\pi$"])
    axis2.legend(loc="upper right")
    axis2.set_xlabel('Definitionsbereich der Abbildung')
    axis2.set_ylabel('Werte der Abbildung')
    plt.show()

def fehlerplot(plotbereich, diff_objct, h_arr):
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
    plotbereich.loglog(h_arr, err_array1, 'g', label='Fehler in erster Ableitung')
    plotbereich.loglog(h_arr, err_array2, 'k', label='Fehler in zweiter Ableitung')
    plotbereich.loglog(h_arr, h_arr, 'g', ls="--", label=r'$y = h$')
    plotbereich.loglog(h_arr, (h_arr)**2, 'k', ls="--", label=r'$y = h^2$')
    plotbereich.loglog(h_arr, (h_arr)**3, 'b', ls="--", label=r'$y = h^3$')

    plotbereich.set_title('Absoluter Fehler in Abhängigkeit von der Schrittweite')
    plotbereich.set_xlabel(r'Schrittweite $h$')
    plotbereich.set_ylabel('Absoluter Fehler')

if __name__ == "__main__":
    main()
