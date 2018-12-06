"""
sparse.py stellt die Klasse Sparse zur Verfuegung, mit der die Matrix A^(d) fuer d=1,2,3
bestimmt und analysiert werden kann.
"""
import numpy as np
from scipy import linalg


class hilbert(object):
    """
    Diese klasse stellt Hilbert-Matrizen zur Verfuegung. 

    Attribute:

        dim (int):
            Dimension der Matrix.
    """
    def __init__(self, dim):
        """
        Initialisiert ein neues Sparse-Objekt.

        Input:

            dim (int):
                Dimension der Hilbertmatrix

        Return: -
        """
        self.dim = dim
        self.hil_matr = linalg.hilbert(self.dim)
        self.inv_hil_matr = linalg.invhilbert(self.dim)

    def return_hil_matr(self, inv=False):
        if inv == False:
            return self.hil_matr
        return self.inv_hil_matr


test_obj = hilbert(2)

inverse = True

print(test_obj.return_hil_matr(inv=inverse))
