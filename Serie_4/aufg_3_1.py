import numpy as np
from scipy import linalg as lina

class Kl_quad(object):
    """
    Diese Klasse macht etwas schoenes. #TODO ergaenzen
    """
    def __init__(self, a_matr, r_s):
        """
        Macht Sachen #TODO ergaenzen

        Input:

            dim (int):
                Raumdimension des zu untersuchenden Gebietes.
            #TODO ergaenzen

        Return: -
        """
        self.a_matr = a_matr
        self.r_s = r_s

    def qr_zerl(self):
        """
        Gibt die Q-R-Zerlegung der Matrix A zurück.

        Input: -

        Return:

                (tupel von bumpy.ndarrays):
                    Die Matrizen Q und R
        """

        return lina.qr(self.a_matr)

    def rang_pruef(self, eps=10*-10):
        """
        Ueberprueft, ob die Matrix A maximalen Spaltenrang hat. Dies ist äquivalent dazu, dass
        alle Diagonalelemente der Matrix R aus der Q-R-Zerlegung alle nicht 0 sind:
        """
        r_matr = self.qr_zerl()[1]
        anz_spalten = self.a_matr.shape[1]

        check = False

        arr = np.arange(anz_spalten)

        diag = r_matr[arr,arr]

        norm = lina.norm(diag, ord=np.inf)

        if norm > eps:
            return True
        else:
            return False

    def lgs_lsg(self):
        """
        Loest das Gleichungssystem Ax=b unter expliziter Ausnutzung der Q-R-Zerlegung.
        """
        q_matr, r_matr = self.qr_zerl()

        # modifizierte rechte Seite:

        r_s_mod = np.dot(q_matr.transpose(),self.r_s)
        return lina.solve_triangular(r_matr, r_s_mod, lower=False)

    def res(self):
        """
        Gibt das Residuum zurueck.
        """

        r_vec = self.a_matr*self.lgs_lsg()-r_s
        r_norm = lina.norm(r_vec, ord=np.inf)

        return r_vec, r_norm

    def kond(self):
        """
        Berechnet die Kondition von A bzw. A^T*A.
        """
        kond_a = lina.cond(a_matr, p=np.inf)
        kond_ata = lina.cond(a_matr.transpose()*a_matr, p=np.inf)

        return kond_a, kond_ata


if __name__ == "__main__":
    A_MATR = np.array([[1,1],[1,2]])
    B_VEC = np.array([1,2])
    K_Q = Kl_quad(A_MATR, B_VEC)
    print(K_Q.lgs_lsg())

