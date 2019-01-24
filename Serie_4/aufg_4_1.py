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

        norm = lina.norm(diag, ord=2)

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

        # Injektivitaet der Matrix pruefen:

        if not self.rang_pruef():
            raise lina.LinAlgError("Die Koeffizientenmatrix ist nicht injektiv, die Methode der "+
                                   "kleinsten Quadrate kann nicht angewendet werden!")

        q_matr, r_matr = self.qr_zerl()

        # modifizierte rechte Seite:

        r_s_mod = np.dot(q_matr.transpose(), self.r_s)

        # quadratischer Anteil der Matrix R (obere Dreiecksmatrix) und zugehoeriger
        # Loesungsvektor:

        anz_spalt = r_matr.shape[1]
        r_matr_red = r_matr[:anz_spalt]
        r_s_mod_red = r_s_mod[:anz_spalt]

        #Loesung durch Rueckwaertseinsetzen:

        return lina.solve_triangular(r_matr_red, r_s_mod_red, lower=False)

    def res(self):
        """
        Gibt das Residuum r=Ax-b und dessen Norm zurueck.

        Input: -

        Return:

            (Tupel aus numpy.ndarray und float):
                Residuum und Norm des Residuums.
        """
        r_vec = np.dot(self.a_matr, self.lgs_lsg()) - self.r_s
        r_norm = lina.norm(r_vec, ord=2)

        return r_vec, r_norm

    def kond(self):
        """
        Berechnet die Kondition von A bzw. A^T*A.

        Input: -

        Return:

            (Tupel aus floats):
                Kondition von A und von A^T*A.
        """

        # Berechnung der Moore-Penrose-Pseudoinversen nach der Formel
        # A^+ = (A^T*A)^-1 * A^T:

        a_pinv = np.dot(lina.inv(np.dot(self.a_matr.transpose(), self.a_matr)),
                        self.a_matr.transpose())

        # Kondition berechnet sich als ||A||*||A^+||:

        kond_a = lina.norm(a_pinv, ord=np.inf) * lina.norm(self.a_matr, ord=2)

        # Fuer die Kondition der quadratischen Matrix A^T*A wird die numpy-Implementierung
        # verwendet:

        kond_ata = np_lina.cond(np.dot(self.a_matr.transpose(), self.a_matr), p=2)

        return kond_a, kond_ata


if __name__ == "__main__":

    # Test der Funktionaitaet:

    A_MATR = np.array([[1, 2], [1, 0.5], [1, 0.2], [1, 4]])
    B_VEC = np.array([1, 1, 2, 5])
    K_Q = KlQuad(A_MATR, B_VEC)
    print(K_Q.lgs_lsg(), "\n")
    print(K_Q.kond())
