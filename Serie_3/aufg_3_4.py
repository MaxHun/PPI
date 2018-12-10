import numpy as np
from hilbertmatr import Hilbert
from sparse_erw import Sparse


def plot_kond(matr, plotber, m_max):
    """
    Plottet die Kondition der Bandmatrizen bzw. der Hilbert-Matrix in Abhaengigkeit von der
    Matrixgroesse m.
    """
    m_arr = np.arange(m_max +1)
    kond_hil_arr = np.zeros(m_max+1)
    kond_a_matr = np.zeros(3,m_max+1)
    #kond_a_2 = np.zeros(m_max+1)
    #kond_a_3 = np.zeros(m_max+1)
    for m_wert in m_arr:
        hil_matr = Hilbert(m_wert)
        kond_hil_arr[m_wert] = hil_matr.kond_hil_zs()
        for dim in [1,2,3]:
           a_matr = Sparse(dim, int(m**(1/d)+1))
           kond_a_matr[dim][m] = a_matr.kond_a_d_zs() # Hier weiter

if __name__ == "__main__":
    plot_kond(1,2,3)
    TEST = Hilbert(0)
    #print(TEST.return_hil_matr())
