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

def plot_kond(plotber, m_max, matr_type):
    """
    Plottet die Kondition der Bandmatrizen bzw. der Hilbert-Matrix in Abhaengigkeit von der
    Matrixgroesse m.

    Input:

        plotber (axis-Objekt):
            Plotbereich, in den geplottet werden soll
        m_max (int):
            Maximale Matrixgroesse.
        matr_type (string):
            Bestimmt die Matrixart, die untersucht wird.
            Moeglichkeiten: Hilbertmatrix ("hil") oder
            Bandmatrix für d=1,2,3 ("a").
    """
    # Array aus m-Werten:

    m_arr = 1 + np.arange(m_max)

    if matr_type == "hil":
        kond_hil_arr = np.zeros(m_max)
        for m_wert in m_arr:
            hil_matr = Hilbert(m_wert)
            kond_hil_arr[m_wert-1] = hil_matr.kond_hil_zs()
        plotber.semilogy(m_arr, kond_hil_arr, "o", markerfacecolor="None",
                         label="$H_m$")
    
    elif matr_type == "a":
        for dim in [1, 2, 3]:
            
            # Diskretisierung muss aus Matrixgroesse berechnet werden. Dabei soll
            # nur n >= 3 betrachtet werden:
            
            n_arr = np.unique((m_arr**(1/dim)+1).astype(int))
            n_arr = n_arr[np.where(n_arr >= 3)]
            
            # Zurückgewinnung der passenden m-Werte und Berechnen der Kondition.

            m_arr_a = (n_arr - 1)**dim
            kond_a_matr = np.zeros(len(n_arr))
            for ind, n_wert in enumerate(n_arr):
                a_matr = Sparse(dim, n_wert)
                kond_a_matr[ind] = a_matr.kond_a_d_zs()
            plotber.semilogy(m_arr_a, kond_a_matr, "o", markerfacecolor="None",
                             label=r"$A^{{({})}}$".format(dim))
    else:
        # Falls eine inkorrekte Eingabe für matr_type erfolgte:
        raise ValueError("Bitte uebergeben Sie einen gueltigen Matrixtyp (\"hil\" " +
                         "fuer Hilbert-Matrizen und" +
                         " \"a\" fuer die Bandmatrizen)!")

def plot_nn(plotber, m_max):
    """
    Plottet die (absolute) Anzahl der Nichtnulleintraege der Koeffizientenmatrix A^(d)
    
    Input:

        plotber (axis-Objekt):
            Plotbereich, in den geplottet werden soll
        m_max (int):
            Maximale Matrixgroesse.
    """
    
    m_arr = 1 + np.arange(m_max)
    colors = ["r", "g", "b"]
    for dim in [1, 2, 3]:

        # Berechnung von n wie in der vorherigen Funktion:

        n_arr = np.unique((m_arr**(1/dim)+1).astype(int))
        n_arr = n_arr[np.where(n_arr >= 3)]
        m_arr_a = (n_arr - 1)**dim
        
        nn_a_matr = np.zeros(len(n_arr))
        nn_a_matr_lu = np.zeros(len(n_arr))
        for ind, n_wert in enumerate(n_arr):
            a_matr = Sparse(dim, n_wert)
            nn_a_matr[ind] = a_matr.anz_nn_abs()
            nn_a_matr_lu[ind] = np.sum(a_matr.anz_nn_lu_abs())

        # Doppelt-logarithmischer Plot:

        plotber.loglog(m_arr_a, nn_a_matr, "o", markerfacecolor="None",
                       label=r"Koeffizientenmatrix $A^{{({})}}$".format(dim),
                       color=colors[dim-1])
        plotber.loglog(m_arr_a, nn_a_matr_lu, "^", markerfacecolor="None",
                       label=r"Dreieckszerlegung von $A^{{({})}}$".format(dim),
                       color=colors[dim-1])

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
            Bandmatrix für d=1,2,3 ("a").
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
            lsg = a_matr.lgs_lsg(r_s)
            fehl_a_matr[ind] = lina.norm(lsg-ex_lsg_arr[ind], ord=np.inf)
        plotber.loglog(m_arr, fehl_a_matr, "o", markerfacecolor="None")
    else:

        raise ValueError("Bitte uebergeben Sie einen gueltigen Matrixtyp (\"hil\" " +
                         "fuer Hilbert-Matrizen und" +
                         " \"a\" fuer die Bandmatrizen)!")

def plot_res(plotber, r_s_arr, matr_type, dim=1):
    """
    Plottet das  Resiuduum.
    """
    m_arr = np.vectorize(len)(r_s_arr)
    if matr_type == "hil":
        res_hil_arr = np.zeros(len(r_s_arr))
        for ind, r_s in enumerate(r_s_arr):
            hil_matr = Hilbert(len(r_s))
            matr = hil_matr.return_hil_matr()
            lsg = hil_matr.lgs_lsg(r_s)
            res_hil_arr[ind] = lina.norm(matr*lsg - r_s, ord=np.inf)
        plotber.loglog(m_arr, res_hil_arr, "o", markerfacecolor="None")
    elif matr_type == "a":
        res_a_matr = np.zeros(len(r_s_arr))
        for ind, r_s in enumerate(r_s_arr):
            n_wert = len(r_s_arr[ind])**(1/dim)+1
            a_matr = Sparse(dim, n_wert)
            lsg = a_matr.lgs_lsg(r_s)
            matr = a_matr.return_mat_d_csc()
            res_a_matr[ind] = lina.norm(matr*lsg - r_s, ord=np.inf)
        plotber.loglog(m_arr, res_a_matr, "o", markerfacecolor="None")
    else:
        # Falls eine inkorrekte Eingabe für matr_type erfolgte:
        raise ValueError("Bitte uebergeben Sie einen gueltigen Matrixtyp (\"hil\" " +
                         "fuer Hilbert-Matrizen und" +
                         " \"a\" fuer die Bandmatrizen)!")
        
if __name__ == "__main__":
    fig, ax_12 = plt.subplots(2, 2, figsize=(20, 10))
    ax_1 = ax_12[0][0]
    ax_2 = ax_12[1][0]
    ax_3 = plt.subplot(122)
    plot_kond(ax_1, 125, "a")
    

    plot_kond(ax_2, 125, "hil")
    plot_nn(ax_3, 125)
    x_arr = np.logspace(0, np.log10(125))
    ax_3.plot(x_arr, 2*x_arr**2, label=r"n^2")
    ax_1.legend()
    ax_2.legend()
    ax_3.legend()
    plt.show()
