import numpy as np
from hilbertmatr import Hilbert
from sparse_erw import Sparse
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


def plot_kond(plotber, m_max, matr_type):
    """
    Plottet die Kondition der Bandmatrizen bzw. der Hilbert-Matrix in Abhaengigkeit von der
    Matrixgroesse m.
    """
    m_arr = 1 + np.arange(m_max)
    kond_hil_arr = np.zeros(m_max)
    print(len(m_arr), len(kond_hil_arr))
    kond_a_matr = np.zeros([3, m_max])
    #kond_a_2 = np.zeros(m_max+1)
    #kond_a_3 = np.zeros(m_max+1)
    #print(m_arr)
    print("m_arr", m_arr)


    if matr_type == "hil":
        kond_hil_arr = np.zeros(m_max)
        for m_wert in m_arr[:-1]:
            hil_matr = Hilbert(m_wert)
            kond_hil_arr[m_wert] = hil_matr.kond_hil_zs()
        plotber.semilogy(m_arr, kond_hil_arr, "o", markerfacecolor="None")
    elif matr_type == "a":
        #kond_a_matr = np.zeros([3,m_max])
        for dim in [1,2,3]:
            i = 0
            print(np.unique((m_arr**(1/dim)+1).astype(int)))
            n_arr = np.unique((m_arr**(1/dim)+1).astype(int))
            n_arr = n_arr[np.where(n_arr>=3)]
            print("Anzahl n-Werte:", len(n_arr))
            print(dim, n_arr)
            m_arr_a = (n_arr - 1)**dim
            kond_a_matr = np.zeros(len(n_arr))
            for n_wert in n_arr:
                a_matr = Sparse(dim, n_wert)
                kond_a_matr[i] = a_matr.kond_a_d_zs()
                i += 1
            plotber.semilogy(m_arr_a, kond_a_matr, "o", markerfacecolor="None")
    else:
        raise ValueError("Bitte uebergeben Sie einen gueltigen Matrixtyp (\"hil\" " +
                         "fuer Hilbert-Matrizen und" +
                         " \"a\" fuer die Bandmatrizen)!")

def plot_nn(plotber, m_max):

    for dim in [1,2,3]:
        
       #####Hier weiter 

if __name__ == "__main__":
    fig, ax_1 = plt.subplots(1,1)
    plot_kond(ax_1,125, "hil")
    TEST = Hilbert(0)
    plt.show()
