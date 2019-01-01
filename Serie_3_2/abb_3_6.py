"""
Dieses Skript erstellt die Plots zu Aufgabe 3.6.
"""


import numpy as np
from hilbertmatr import Hilbert
from sparse_erw import Sparse
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from scipy import linalg as lina
#from scipy.sparse import linalg as sp_lina
#import scipy.sparse as sp

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
matplotlib.rcParams.update({'font.size': 33})
plt.rc('text', usetex=True)
#plt.rc('font', family='Open Sans')
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',r"\usepackage{nicefrac}"]

groess=15
lw=4


def plot_kond_hil(plotber, m_max):
    """
    Plottet die Kondition der Hilbert-Matrix in Abhaengigkeit von der
    Matrixgroesse m.

    Input:
        plotber (axis-Objekt):
            Plotbereich, in den geplottet werden soll
        m_max (int):
            Maximale Matrixgroesse.
    """
    # Array aus m-Werten:

    m_arr = 1 + np.arange(m_max)

    kond_hil_arr = np.zeros(m_max)
    for m_wert in m_arr:
        hil_matr = Hilbert(m_wert)
        kond_hil_arr[m_wert-1] = hil_matr.kond_hil_zs()
    plotber.semilogy(m_arr, kond_hil_arr, "-", markerfacecolor="None", markersize=groess,
                     lw=lw,label="Kondition von $H_m$", color="violet")

def ex_lsg_hil_ev(ind, dim):
    """
    Liefert die exakte Loesung des Problems H_dim*x=e_ind, wobei
    e_ind der ind-te Einheitsvektor ist.

    Input:
        ind (int):
            Gibt an, welcher Einheitsvektor verwendet wird.
        dim (int):
            Dimension der Hilbert-Matrix.

    Return:
        (numpy.ndarray):
            Exakte Loesung des Gleichungssystems.
    """
    hil = Hilbert(dim)
    hil_inv_matr = hil.return_hil_matr(inv=True)

    # ind-te Spalte der Inversen zurueckgeben:

    return hil_inv_matr[:, ind -1]

def evec(ind, dim):
    """
    Gibt den ind-ten Einheitsvektor zurueck.

    Input:
        ind (int):
            Gibt an, welcher Einheitsvektor zurueckgegeben wird.
        dim (int):
            Dimension des Vektors.
    Return:
        (numpy.ndarray):
            ind-ter Einheitsvektor
    """
    ev_arr = np.zeros(dim)
    ev_arr[ind-1] = 1

    return ev_arr



def plot_fehl(plotber, r_s_arr, ex_lsg_arr, matr_type, dim=1):
    """
    Plottet den Fehler der numerischen Loesung im Vergleich zur exakten Loesung.

    Input:
        plotber (axis-Objekt):
            Plotbereich, in den geplottet werden soll
        r_s_arr (list oder array aus numpy.ndarrays):
            Liste aus rechten Seiten.
        ex_lsg_arr (list oder array aus numpy.ndarrays):
            Liste aus entsprechenden exakten Loesungen.
        matr_type (string):
            Bestimmt die Matrixart, die untersucht wird.
            Moeglichkeiten: Hilbertmatrix ("hil") oder
            Bandmatrix fuer d=1,2,3 ("a").
        dim (int, Standard: 1):
            Wird nur fuer die Bandmatrizen benoetigt und gibt deren Dimension an.
    """

    # Die Matrixgroesse ergibt sich direkt aus den Vektoren:

    m_arr = np.vectorize(len)(r_s_arr)


    if matr_type == "hil":

        # Berechnung und Plotten des Fehlers:

        fehl_hil_arr = np.zeros(len(r_s_arr))
        for ind, r_s in enumerate(r_s_arr):
            hil_matr = Hilbert(len(r_s))
            lsg = hil_matr.lgs_lsg(r_s)
            fehl_hil_arr[ind] = lina.norm(lsg - ex_lsg_arr[ind], ord=np.inf)
        plotber.loglog(m_arr, fehl_hil_arr, "o", markerfacecolor="None", markersize=groess)


    elif matr_type == "a":

        # Berechnung und Plotten des Fehlers:

        fehl_a_matr = np.zeros(len(r_s_arr))
        for ind, r_s in enumerate(r_s_arr):

            # Berechnung von n und des Fehlers:

            n_wert = len(r_s_arr[ind])**(1/dim)+1
            a_matr = Sparse(dim, n_wert)
            lsg = a_matr.lgs_lsg(r_s)
            fehl_a_matr[ind] = lina.norm(lsg-ex_lsg_arr[ind], ord=np.inf)
        plotber.loglog(m_arr, fehl_a_matr, "o", markerfacecolor="None")

    else:
        # Falls eine inkorrekte Eingabe fuer matr_type erfolgte:
        raise ValueError("Bitte uebergeben Sie einen gueltigen Matrixtyp (\"hil\" " +
                         "fuer Hilbert-Matrizen und" +
                         " \"a\" fuer die Bandmatrizen)!")

def main():
    """
    Hauptprogramm, in dem die Plots fuer Aufgabe 3.6. erstellt werden.

    Input:-

    Return:-
    """

    log2_m_max = 7
    m_arr = 2**np.arange(log2_m_max + 1)

    max_norm = np.zeros(len(m_arr))
    for m_ind, m_wert in enumerate(m_arr):
        hil = Hilbert(m_wert)
        # Matrix, deren Spalten aus exakter Loesung bestehen:
        ex_lsg_matr = hil.return_hil_matr(inv=True)
        norm_ind_arr = np.zeros(m_wert)
        for lis_ind, ind in enumerate(1 + np.arange(m_wert)):
            norm_ind_arr[lis_ind] = np.amax(np.abs(hil.lgs_lsg(evec(ind, m_wert)) -
                                                   ex_lsg_matr[:, ind-1]))
            max_norm[m_ind] = np.amax(norm_ind_arr)
    plt.figure(figsize=(20, 20))
    ax_1 = plt.subplot(111)
    
    plot_kond_hil(ax_1, 130)
    plt.loglog(m_arr, max_norm, "x", markerfacecolor="None", basex=2, markersize=groess,
               label=r"$\max\limits_{i=1,\dots,m}|| \tilde{x}^{(i)}-x^{(i)}||_\infty$",
               markeredgewidth=lw)
    plt.xlabel(r"Matrixgroesse $m$")
    plt.ylabel("Fehler bzw. Kondition")
    plt.subplots_adjust(top=0.98, left=0.08, right=0.99, bottom=0.07)
    ax_1.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax_1.tick_params(right=True, direction='in',which='both')    
    ax_1.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
    #ax_1.set_ylim(1e-5,1e+206)
    #print(ax_1.get_ylim()[1])
    plt.legend()
    plt.savefig("Bericht/Bilder/hil_kond_fehl.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
