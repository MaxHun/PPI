"""
Dieses Skript besteht im Wesentlichen aus der Klasse KlQuad, die das Loesen von ueberbestimmten
Gleichungssystemen mit der Methode der kleinsten Quadrate ermoeglicht.
"""
import numpy as np
from scipy import linalg as lina
from numpy import linalg as np_lina # wird fuer Kondition benoetigt
class KlQuad(object):
    """
    Diese Klasse stellt die Methode der kleinsten Quadrate zur Verfuegung, mit deren Hilfe
    ueberbestimmte Gleichungssysteme geloest werden koennen.
    """
    def __init__(self, a_matr, r_s):
        """
        Konstruktor der KlQuad-Klasse.

        Input:

            a_matr (array_like):
                Zu untersuchende (i.A. nicht quadratische) Matrix.
            r_s (numpy.ndarray):
                Rechte Seite b des zu untersuchenden (ueberbestimmten) Gleichungssystems Ax=b.

        Return: -
        """
        self.a_matr = a_matr
        self.r_s = r_s

    def qr_zerl(self):
        """
        Gibt die Q-R-Zerlegung der Matrix A zurück.

        Input: -

        Return:

                (Tupel von numpy.ndarrays):
                    Die Matrizen Q und R.
        """

        return lina.qr(self.a_matr)

    def rang_pruef(self, eps=10**-12):
        """
        Ueberprueft, ob die Matrix A maximalen Spaltenrang hat. Dies ist äquivalent dazu, dass
        alle Diagonalelemente der Matrix R aus der Q-R-Zerlegung alle nicht 0 sind. Aufgrund
        numerischer Fehler werden dia Diagonaleintraege von R nicht mit 0, sondern mit einer
        zu wählenden kleinen Zahl eps verglichen (Standard:10**-12).

        Input:

            eps (float, optional, Standardwert: 10**-12)

        Return:

            (bool):
                Wahrheitswert der Aussage "A hat vollen Spaltenrang"
        """
        r_matr = self.qr_zerl()[1]
        anz_spalten = self.a_matr.shape[1]

        arr = np.arange(anz_spalten)

        diag = r_matr[arr, arr]

        norm = lina.norm(diag, ord=-np.inf)

        return bool(norm > eps)

    def lgs_lsg(self):
        """
        Loest das Gleichungssystem Ax=b unter expliziter Ausnutzung der Q-R-Zerlegung. Dabei wird
        die obere Dreiecksgestalt von R und die Orthogonalität von Q ausgenutzt.

        Input: -

        Return:

            (numpy.ndarray):
                Loesungsvektor von Ax=b.
        """
        q_matr, r_matr = self.qr_zerl()

        # modifizierte rechte Seite:

        r_s_mod = np.dot(q_matr.transpose(), self.r_s)

        #Loesung durch Rueckwaertseinsetzen:
        #print("\n\n", r_matr[:,r_matr[1]], "\n")
        print(r_matr[:2]) #TODO Funktioniert noch nicht, hier weiter
        return lina.solve_triangular(r_matr[:2], r_s_mod, lower=False)

    def res(self):
        """
        Gibt das Residuum r=Ax-b und dessen Norm zurueck.

        Input: -

        Return:

            (Tupel aus numpy.ndarray und float):
                Residuum und Norm des Residuums.
        """

        r_vec = self.a_matr*self.lgs_lsg()-self.r_s
        r_norm = lina.norm(r_vec, ord=np.inf)

        return r_vec, r_norm

    def kond(self):
        """
        Berechnet die Kondition von A bzw. A^T*A.

        Input: -

        Return:

            (Tupel aus floats):
                Kondition von A und von A^T*A.
        """
        kond_a = np_lina.cond(self.a_matr, p=np.inf)
        kond_ata = np_lina.cond(self.a_matr.transpose()*self.a_matr, p=np.inf)

        return kond_a, kond_ata


if __name__ == "__main__":
    A_MATR = np.array([[1, 2], [1, 1],[1,0.5]])
    B_VEC = np.array([1, 2,0.5])
    K_Q = KlQuad(A_MATR, B_VEC)
    print(K_Q.lgs_lsg(), "\n")
    #print(K_Q.kond())
