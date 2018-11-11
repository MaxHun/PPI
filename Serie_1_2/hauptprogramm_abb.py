"""
Dieses Programm dient zur Veranschaulichung der Fehler bei der Approximation der ersen und
zweiten Ableitungen der Sinus Funtion durch die Methode der Vorwaertsdifferenz. Ausgegeben
werden 2 pyplot-figures. Diese zeigen zum einen die aproximierten und exakten Ableitungen
des Sinus an, zum anderen werden die abs. Fehler der approximierten Ableitungen in
Abhaengigkeit von der Differenziationsschrittweite h geplottet. Dies wird mit dem Verhalten
der entsprechenden Fehler für f(x)=sin(j*x) graphisch verglichen. Hierbei ist das j vom
Nutzer durch einen Schieberegler waehlbar.

A. Hnatiuk
M. Huneshagen
"""
from differenzieren import negsin
from matplotlib.widgets import Slider
import differenzieren
import functools
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
#import differenzieren
#rom differenzieren import negsin
#from matplotlib.widgets import Slider


def sin_j(arg, j=1):
    """
    Diese Funktion übernimmt ein Argument arg und einen Parameter j und gibt denn Wert von
    sin(j*x) an der Stelle x=arg zurück.
    Input:

        arg (float):
            Stelle, die untersucht werden soll.
        j (float, optional, Standard: 1):
            Parameter, um den arg multipliziert wird.

    Return: -
    """
    return np.sin(arg*j)

def cos_j(arg, j=1):
    """
    Ableitung von sin_j.
    Input:

        arg (float):
            Stelle, die untersucht werden soll.
        j (float, optional, Standard: 1):
            Parameter, um den arg multipliziert wird.

    Return: -
    """
    return j*np.cos(arg*j)

def negsin_j(arg, j=1):
    """
    Zweite Ableitung von sin_j.
    Input:

        arg (float):
            Stelle, die untersucht werden soll.
        j (float, optional, Standard: 1):
            Parameter, um den arg multipliziert wird.

    Return: -
    """
    return -j**2*np.sin(arg*j)

def main():
    """
    Dieses Hauptprogramm dient dem Plotten des Sinus und seiner Ableitungen (exakt und approx.)
    sowie dem Untersuchen des bei der Berechnung maximal gemachten Fehlers. Darüber hinaus erfolgt
    der Vergleich mit der Funktion sin(j*x). Dazu werden zwei figures angelegt.
    Input: -

    Return: -
    """

    # Anlegen einer Figure mit 2 Subplots:
    matplotlib.rcParams.update({'font.size': 25})
    plt.rc('text', usetex=True)
    plt.rc('font', family='Open Sans')
    matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',r"\usepackage{nicefrac}"]
    fig, axis1 = plt.subplots(1,1 , figsize=(20, 16), sharey=True)
    h_arr = np.logspace(-18, 2, 1000)           #Werte der getesteten Schrittweiten
    p_werte = np.linspace(0, np.pi, 1000)

    # Erstellung eines Differenzieren-Objektes:

    sin_obj = differenzieren.Differenzieren(np.sin, np.cos, negsin, p_werte)

    # Erstellen von pyplot.Axes-Elementen für die Slider: Erstellung der Slider. Es wird ein
    # Slider für grosse j und ein Slider fuer kleine j verwendet, um zwischen 0 und 1 feinere
    # Auswahl zu ermöglichen. Der verwendete Wert für j wird im Plotbereich angegeben:

    #balken_oben = plt.axes([0.3, 0.05, 0.4, 0.03])
    #balken_unten = plt.axes([0.3, 0.01, 0.4, 0.03])
    #j_slider_kleine_j = Slider(balken_oben, r'Waehlen Sie ein $j\in[0,1]$:', 0, 1, valinit=1,
     #                          valstep=0.0001)
    #j_slider_grosse_j = Slider(balken_unten, r'Waehlen Sie ein $j\in[1,100]$:', 1, 100,
     #                          valinit=1, valstep=0.5)


    # Da die Funktion slider.on_changed nur ein Argument übernimmt, müssen zuvor die keyword-
    # Arguments für neues_j per functools.partial übergeben werden:

    #axis2_neues_kleines_j = functools.partial(neues_j, plotbereich=axis2, slider=j_slider_kleine_j,
      #                                        p_werte=p_werte, h_arr=h_arr)
    #j_slider_kleine_j.on_changed(axis2_neues_kleines_j)
    #axis2_neues_grosses_j = functools.partial(neues_j, plotbereich=axis2, slider=j_slider_grosse_j,
      #                                        p_werte=p_werte, h_arr=h_arr)
    #j_slider_grosse_j.on_changed(axis2_neues_grosses_j)

    # Plotten des Fehlers für sin in den linken Subplot:

    fehlerplot(axis1, sin_obj, h_arr)

    # Beschriftungen etc.:

    axis1.set_xlabel(r'Differenziationsschrittweite $h$')
    axis1.set_ylabel('Fehler der Ableitung')
    #axis1.xaxis.set_label_coords(1.05, -0.045)
    #axis2.text(0.3, 10**-12, "Wählen Sie  ein j mithilfe des Sliders unten")
    #axis1.legend(ncol=4,loc="lower center" , facecolor="w")
    #fig.suptitle("Fehlerverhalten der Approximation der ersten und zweiten Ableitung")
    plt.subplots_adjust(wspace=0.0, top=0.94, bottom=0.14)
    #plt.xlim(10**-4,10**2)
    ########################## neue Figure ######################################################

    # Ab hier wird die figure zur Darstellung des Sinus bearbeitet:

    #fig2, axis_arr = plt.subplots(2, 2, figsize=(18, 11))
    #axis_arr = axis_arr.flatten()

    # Das Plotten erfolgt durch die Differenzieren-Funktionen plotfkt_exakt bzw. plotfkt_approx
    # weitgehend analog zu Serie 1:

    #colors = ["r", "g", "b"]
    #schrittwt = [np.pi/3, np.pi/4, np.pi/5, np.pi/10]
    #nummer = [3, 4, 5, 10]
    #sin_obj.plotfkt_exakt(axis_arr[0], color="m", label=r"$\sin(x)$")
    #sin_obj.plotfkt_exakt(axis_arr[1], color="m")
    #sin_obj.plotfkt_exakt(axis_arr[2], color="m")
    #sin_obj.plotfkt_exakt(axis_arr[3], color="m")
    #for nbr in [0, 1, 2, 3]:
    #    for grad in [1, 2]:
    #        if nbr == 0:
    #            sin_obj.plotfkt_exakt(axis_arr[nbr], grad=grad, color=colors[grad-1], alpha=0.3,
    #                                  lw=4, label="{}. Ableitung, exakt".format(grad))
    #        else:
    #            sin_obj.plotfkt_exakt(axis_arr[nbr], grad=grad, color=colors[grad-1], alpha=0.3,
    #                                  lw=4)
    #        if nbr == 0:
    #            sin_obj.plotfkt_approx(schrittwt[nbr], axis_arr[nbr], grad=grad,
    #                                   color=colors[grad-1], ls="--",
    #                                   label="{}. Ableitung, approx.".format(grad))
    #        else:
    #            sin_obj.plotfkt_approx(schrittwt[nbr], axis_arr[nbr], grad=grad,
    #                                   color=colors[grad-1], ls="--")
     #   # Beschriftungen etc:
#
#        axis_arr[nbr].set_title(r'$h=\frac{}{}$'.format(r"{\pi}", "{"+str(nummer[nbr])+"}"))
#        axis_arr[nbr].set_xlim(0, np.pi)
#        axis_arr[nbr].set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
 #       axis_arr[nbr].set_xticklabels([r"$0$", r"$\frac{\pi}{4}$", r"$\frac{\pi}{2}$",
  #                                     r"$\frac{3\pi}{4}$", r"$\pi$"])
  #      axis_arr[nbr].set_xlabel('Definitionsbereich der Abbildung')
  #      axis_arr[nbr].set_ylabel('Werte der Abbildung')
  #  fig2.suptitle(r"$\sin x$ und seine ersten beiden Ableitungen, exakt und approximiert mit " +
  #                r"verschiedenen Schrittweiten $h$")
  #  fig2.legend(loc="right")
  #  plt.subplots_adjust(right=0.87, left=0.05, bottom=0.12)
#
#
    plt.show()




def neues_j(slider, plotbereich, p_werte, h_arr):
    """
    Diese Funktion dient dem Erstellen eines neuen Fehlerplots, wenn ein neuer j-Wert
    vom Nutzer auf dem Schieberegler ausgewählt wurde. Dazu wird ein neues Differenzieren-
    Objekt angelegt.
    Input:
        slider (matplotlib.widgets.Slider-Objekt):
            Zu verwendender Slider.
        plotbereich (pyplot.Axes-Objekt):
            Plotbereich, in den geplottet werden soll.
        p_werte (numpy.ndarray aus floats):
            Plotpunkte, an denen die Funktionen geplottet bzw. für die Fehlerbestimmung aus-
            gewertet werden.i
        h_array (numpy.ndarray aus floats):
                    Array mit den Schrittweiten.

    Return: -
    """

    # Vorherigen Plot entfernen:

    plotbereich.cla()

    # j-Wert ermitteln und in plotbereich plotten:

    j = slider.val
    plotbereich.text(1e-3, 1e-30, "j={0:.3f}".format(j))
    plt.gcf().canvas.draw_idle()

    # Da der Konstruktor der Differenzieren-Klasse keine keyword-Arguments für die zu
    # untersuchende Funktion übernehmen kann, muss das j zuvor per functools.partial
    # an die entspr. Funktionen übergeben werden:

    sin_j_fkt = functools.partial(sin_j, j=j)
    cos_j_fkt = functools.partial(cos_j, j=j)
    negsin_j_fkt = functools.partial(negsin_j, j=j)
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
            Array mit den Schrittweiten.

    Return: -
    """
    err_array1 = np.vectorize(diff_objct.err_abl)(h_arr, grad=1)   #Fehler 1. Ableitung
    err_array2 = np.vectorize(diff_objct.err_abl)(h_arr, grad=2)    #Fehler 2. Ableitung

    if labeling:
        mult = 1
    else:
        mult = 0

    plotbereich.loglog(h_arr, err_array1, 'g', label='Fehler in erster Ableitung'*mult, lw=3)
    plotbereich.loglog(h_arr, err_array2, 'k', label='Fehler in zweiter Ableitung'*mult, lw=3)
    plotbereich.loglog(h_arr, h_arr, 'g', ls="--", label=r'$y = h$'*mult)
    plotbereich.loglog(h_arr, (h_arr)**2, 'k', ls="--", label=r'$y = h^2$'*mult)
    plotbereich.loglog(h_arr, (h_arr)**3, 'b', ls="--", label=r'$y = h^3$'*mult)
    plotbereich.loglog(h_arr, (h_arr)**-1, 'g', ls="-.", label=r'$y = h^{-1}$'*mult)
    plotbereich.loglog(h_arr, (h_arr)**-2, 'k', ls="-.", label=r'$y = h^{-2}$'*mult)


if __name__ == "__main__":
    main()
