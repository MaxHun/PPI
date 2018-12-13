import numpy as np
from hilbertmatr import Hilbert
from sparse_erw import Sparse
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


def plot_kond(plotber, m_max):
    """
    Plottet die Kondition der Bandmatrizen bzw. der Hilbert-Matrix in Abhaengigkeit von der
    Matrixgroesse m.
    """
    m_arr = 10 + np.arange(m_max)
    kond_hil_arr = np.zeros(m_max)
    print(len(m_arr), len(kond_hil_arr))
    kond_a_matr = np.zeros([3,m_max])
    #kond_a_2 = np.zeros(m_max+1)
    #kond_a_3 = np.zeros(m_max+1)
    #print(m_arr)
    for m_wert in (m_arr-9)[:-2]:
        print((m_arr-9)[:-1])
        hil_matr = Hilbert(m_wert)
        kond_hil_arr[m_wert] = hil_matr.kond_hil_zs()
        for dim in [1,2,3]:
           #print(int(m_wert**(1/dim)+1)+3)
           a_matr = Sparse(dim, int(m_wert**(1/dim)+1)+3)
           kond_a_matr[dim-1][m_wert] = a_matr.kond_a_d_zs()
    plotber.semilogy(m_arr, kond_hil_arr)

    for dim in [1,2,3]:
        plotber.semilogy(m_arr, kond_a_matr[dim-1])

if __name__ == "__main__":
    fig, ax_1 = plt.subplots(1,1)
    plot_kond(ax_1,100)
    TEST = Hilbert(0)
    plt.show()
