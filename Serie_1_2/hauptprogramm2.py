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
    In dieser Funktion werden die vier Iterationen der Sinus Abbildung mit Ihrer Ableitungen
    geplottet.
    Input:-
    Return:-
    """
    fig, axis = plt.subplots(2, 2, figsize=(18, 11))
    axis = axis.reshape([1, 4])
    print(axis.shape)
    p_werte = np.linspace(0, np.pi, 1000)
    sin_obj = differenzieren.Differenzieren(np.sin, np.cos, negsin, p_werte)
    #Hier werden die Funktion und ihre Ableitungen geplottet
    colors = ["r", "g", "b"]
    schrittwt = [np.pi/3, np.pi/4, np.pi/5, np.pi/10]
    nummer = [3, 4, 5, 10]
    sin_obj.plotfkt_exakt(axis[0, 0], color="m", label=r"$\sin(x)$")
    sin_obj.plotfkt_exakt(axis[0, 1], color="m")
    sin_obj.plotfkt_exakt(axis[0, 2], color="m")
    sin_obj.plotfkt_exakt(axis[0, 3], color="m")
    for nbr in [0, 1, 2, 3]:
        for grad in [1, 2]:
            if nbr == 0:
                sin_obj.plotfkt_exakt(axis[0, nbr], grad=grad, color=colors[grad-1], alpha=0.3,
                                      lw=4, label="{}. Ableitung, exakt".format(grad))
            else:
                sin_obj.plotfkt_exakt(axis[0, nbr], grad=grad, color=colors[grad-1], alpha=0.3,
                                      lw=4)
            if nbr == 0:
                sin_obj.plotfkt_approx(schrittwt[nbr], axis[0, nbr], grad=grad,
                                       color=colors[grad-1], ls="--",
                                       label="{}. Ableitung, approximiert".format(grad))
            else:
                sin_obj.plotfkt_approx(schrittwt[nbr], axis[0, nbr], grad=grad,
                                       color=colors[grad-1], ls="--")
        axis[0, nbr].set_title('Die Funktion und ihre Ableitungen (exakte und approximierte mit'+
                               ' Schrittweite pi/' + str(nummer[nbr])+')')
        axis[0, nbr].set_xlim(0, np.pi)
        axis[0, nbr].set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
        axis[0, nbr].set_xticklabels(["$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$",
                                      r"$\frac{3\pi}{4}$", r"$\pi$"])
        axis[0, nbr].set_xlabel('Definitionsbereich der Abbildung')
        axis[0, nbr].set_ylabel('Werte der Abbildung')
    fig.legend(loc="right center")
    plt.show()

if __name__ == "__main__":
    main()
