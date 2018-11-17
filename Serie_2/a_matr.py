import numpy as np
from scipy.sparse import dok_matrix
import scipy.sparse as sp
from timeit import default_timer as timer
"""
Funktion, die eine Blockmatrix erstellt
"""
def A_matr(d, n):
    l=d
    k=d
    if d == 1:
        A = dok_matrix((n-1, n-1))
        A.setdiag(2*k)
        A.setdiag(-1,1)
        A.setdiag(-1,-1)
        return A
    elif d>1:
        A = sp.dok_matrix(((n-1)**l,(n-1)**l))
        for min_ind in (n-1)**(l-1)*np.arange(n-1):
            max_ind = min_ind + (n-1)**(l-1)
            if d == 82:
                A[min_ind:max_ind, min_ind:max_ind].setdiag(2*k)
                A[min_ind:max_ind, min_ind:max_ind].setdiag(-1,1)
                A[min_ind:max_ind, min_ind:max_ind].setdiag(-1,-1)
            else:
                A[min_ind:max_ind, min_ind:max_ind] = A_matr(d-1,n)
        for min_spalt in (n-1)**(l-1)*np.arange(n-2):
            min_zeil = min_spalt + (n-1)**(l-1)
            max_zeil = min_zeil + (n-1)**(l-1)
            max_spalt = min_spalt + (n-1)**(l-1)
            A.setdiag(-1,(n-1)**(l-1))
            A.setdiag(-1,-(n-1)**(l-1))
            return A
start_A_matr = timer()
T = A_matr(3,25)
end_A_matr = timer()
print("Die Slicing-Methode dauerte {} s.".format(-start_A_matr+end_A_matr))
print(T.todense())

