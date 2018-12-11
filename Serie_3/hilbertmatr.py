"""
sparse.py stellt die Klasse Sparse zur Verfuegung, mit der die Matrix A^(d) fuer d=1,2,3
bestimmt und analysiert werden kann.
"""
import numpy as np
from scipy import linalg as lina


class Hilbert(object):
    """
    Diese Klasse stellt Hilbert-Matrizen zur Verfuegung.

    Attribute:

        dim (int):
            Dimension der Matrix.
    """
    def __init__(self, dim, r_s=None):
        """
        Initialisiert ein neues Sparse-Objekt.

        Input:

            dim (int):
                Dimension der Hilbertmatrix

        Return: -
        """
        self.dim = dim
        self.hil_matr = lina.hilbert(self.dim)
        self.inv_hil_matr = lina.invhilbert(self.dim)
        self.r_s = r_s

    def return_hil_matr(self, inv=False):
        """
        Gibt die Hilbertmatrix oder ihr Inverses zurueck.
        """
        if not inv:
            return self.hil_matr
        return self.inv_hil_matr

    def kond_hil_zs(self):
        """
        Gibt die Kondition der Matrix bezueglich der Zeilensummennorm zurueck.
        """
        norm_matr = lina.norm(self.hil_matr, ord=np.inf)
        norm_matr_inv = lina.norm(self.return_hil_matr(inv=True), ord=np.inf)
        return norm_matr * norm_matr_inv

    def l_u_zerl(self):
        """
        Errechnet die L-U-Zerlegung von A^(d).
        """
        return lina.lu(self.hil_matr)

    def lgs_lsg(self, r_s=None):
        """
        Loest das Gleichungssystem Ax=r_s fuer eine vorgebene rechte Seite unter Ausnutzung der
        Dreieckszerlegung.
        """
        if r_s is None and self.r_s is not None:
            r_s = self.r_s
        elif r_s is  None and self.r_s is  None:
            print("Bitte uebergeben Sie eine gueltige rechte Seite!")
            return True
        p_matr, l_matr, u_matr = self.l_u_zerl()
        r_s_tr = p_matr.transpose()*r_s
        zw_erg = lina.solve(l_matr, r_s_tr) #TODO nochmal nachdenken
        lsg = lina.solve(u_matr, zw_erg)
        return lsg

if __name__ == "__main__":
    TEST_OBJ = Hilbert(6)

    INVERSE = False

    print(TEST_OBJ.return_hil_matr(inv=INVERSE), TEST_OBJ.lgs_lsg(r_s=np.zeros(6))
          , TEST_OBJ.kond_hil_zs())
