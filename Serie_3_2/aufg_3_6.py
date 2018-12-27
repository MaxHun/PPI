"""
Dieses Skript stellt die Loesung zu Aufgabe 3.4 dar, bei der es vor allem um die Analyse
der beiden zuvor bahndelten Matrizentypen und deren Fehleranfaelligkeit geht.
"""


import numpy as np
from hilbertmatr import Hilbert
from sparse_erw import Sparse
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from scipy import linalg as lina
from scipy.sparse import linalg as sp_lina
import scipy.sparse as sp

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
    plotber.semilogy(m_arr, kond_hil_arr, "o", markerfacecolor="None",
                     label="Kondition von $H_m$", color="violet")

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
            Exakte Lösung des Gleichungssystems.
    """
    hil = Hilbert(dim)
    hil_inv_matr = hil.return_hil_matr(inv=True)

    # ind-te Spalte der Inversen zurueckgeben:

    return hil_inv_matr[:,ind -1]

def ev(ind, dim):
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
        plotber.loglog(m_arr, fehl_hil_arr, "o", markerfacecolor="None")


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
    Hauptprogramm, es werden Sachen gemacht
    """ #TODO ergaenzen

    log2_m_max = 7
    m_arr = 2**np.arange(log2_m_max + 1)

    max_norm = np.zeros(len(m_arr))
    for m_ind, m_wert in enumerate(m_arr):
        hil = Hilbert(m_wert)
        # Matrix, deren Spalten aus exakter Loesung bestehen:
        ex_lsg_matr = hil.return_hil_matr(inv=True)
        norm_ind_arr = np.zeros(m_wert)
        for lis_ind, ind in enumerate(1 + np.arange(m_wert)):
            norm_ind_arr[lis_ind] = np.amax(np.abs(hil.lgs_lsg(ev(ind,m_wert)) - ex_lsg_matr[:, ind-1]))#], ord=np.inf)
        max_norm[m_ind] = np.amax(norm_ind_arr)
    plt.figure(figsize=(20,20))
    ax_1 = plt.subplot(111)
    plt.loglog(m_arr, max_norm,"x", markerfacecolor="None", basex=2, 
               label=r"$\max_{i=1,\dots,m}|| \tilde{x}^{(i)}-x^{(i)}||_\infty$")
    plot_kond_hil(ax_1, 130)
    plt.xlabel(r"$m$")
    plt.ylabel("Fehler bzw. Kondition")    
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
    # Erstellen von Subplots:

    #AX_12 = plt.subplots(1, 1, figsize=(20, 10))[1]
    #AX_1 = AX_12[0][0]
    #AX_2 = AX_12[1][0]
    #AX_3 = plt.subplot(122)
#
    # Plotbefehle:

    #plot_kond(AX_1, 125, "a")
#############    plot_kond(AX_2, 125, "hil")
    #plot_nn(AX_3, 125)
    #X_ARR = np.logspace(0, np.log10(125))
    #AX_3.plot(X_ARR, 2*X_ARR**2, "--", label=r"$2\cdot n^2$")

    # Beschriftung:

    #AX_1.set_title(r"Kondition der verschiedenen Matrizen")
    #AX_1.set_ylabel(r"$\kappa$")
#############    AX_2.set_xlabel(r"Matrixgroesse $m$")
#############    AX_2.set_ylabel(r"$\kappa$")
    #AX_3.set_title(r"Nichtnulleintraege der Bandmatrizen $A^{(d)}$")
    #AX_3.set_ylabel(r"Nichtnulleintraege")
    #AX_3.set_xlabel(r"Matrixgroesse $m$")

    # Anpassung des Layouts und Legende:

    #plt.subplots_adjust(hspace=0)
    #AX_1.tick_params(right=True, left=True, top=True, bottom=True, direction='in', which='both')
    #AX_2.tick_params(right=True, left=True, top=True, bottom=True, direction='in', which='both')
    #AX_3.tick_params(right=True, left=True, top=True, bottom=True, direction='in', which='both')
    #AX_1.legend()
    #AX_2.legend()
    #AX_3.legend()
#
#    plt.show()
