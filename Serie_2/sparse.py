"""
sparse.py stellt die Klasse Sparse zur Verfuegung, mit der die Matrix A^(d) fuer d=1,2,3
bestimmt und analysiert werden kann.
"""
import numpy as np
import scipy.sparse as sp


class Sparse(object):
    """
    Diese Klasse erlaubt das Erstellen der Matrizen A^(d) fuer d in [1,2,3]. Diese Matrizen werden
    z. B. fuer die Berechnung der DGL u''(x)=-f(x) verwendet. Es handelt sich bei diesen Matrizen
    um sehr duenn besetzte Block-Band-Matrizen, was die Verwendung von sog. sparse-Matrizen
    in der numerischen Umsetzung nahelegt.

    Attribute:

        dim (int):
            Raumdimension des zu untersuchenden Gebietes.
        dis (numpy.ndarray aus floats):
            Mass fuer die Diskretisierung des zu untersuchenden Gebietes.
        matr (scipy.dok_matrix-Objekt):
            A^(d) mit Diskretisierung dis.
    """
    def __init__(self, dim, dis):
        """
        Initialisiert ein neues Sparse-Objekt.

        Input:

            dim (int):
                Raumdimension des zu untersuchenden Gebietes.
            dis (int):
                bestimmt die Feinheit der Diskretisierung.

        Return: -
        """
        self.dim = dim
        self.dis = dis
        self.matr = self.constr_mat_l_k(dim, dim, dis)

    def constr_mat_l_k(self, k, dim, dis):
        """
        Konstruiert die Matrix A_l(k) mit der gewuenschten Diskretisierung.

        Input:

            k (float):
                Bestimmt den Wert auf der Hauptdiagonalen der untersuchten Matrix (=2*k)
            dim (int, moegliche Werte: 1, 2, 3):
                Raumdimension des betrachteten Gebietes.
            dis (int):
                Diskretisierung des Gebietes.

        Return:
            (scipy.sparse.dok_matrix-Objekt):
                A_l(k) mit der gewuenschten Diskretisierung.
        """
        if dim == 1:

            # Im Falle dim==1 werden die 3 mittleren Diagonalen gemaess Definition befuellt:

            mat = sp.dok_matrix((dis-1, dis-1))
            mat.setdiag(2*k)
            mat.setdiag(-1, 1)
            mat.setdiag(-1, -1)
            return mat
        
        elif dim == 2 or dim == 3:

            # Anlegen der Matrix:

            mat = sp.dok_matrix(((dis-1)**dim, (dis-1)**dim))

            # Per for-Schleife wird auf die (n-1)^(d-1)-dimensionale Diagonale
            # die Matrix A^(d-1) mit gleichem k gelegt (Rekursion):

            for min_ind in (dis-1)**(dim-1)*np.arange(dis-1):
                max_ind = min_ind + (dis-1)**(dim-1)
                mat[min_ind:max_ind, min_ind:max_ind] = self.constr_mat_l_k(k, dim-1, dis)

            # Zudem werden die beiden (n-1)**(l-1)-ten Nebendiagonalen mit -1 befuellt:

            mat.setdiag(-1, (dis-1)**(dim-1))
            mat.setdiag(-1, -(dis-1)**(dim-1))

            return mat

        # Ausgabe bei fehlerhaftem l:
        print("Der Methode constr_A_k_l wurde ein falscher Wert fuer l " +
              "uebergeben. Moeglich sind l=1,2,3")
        return None

    def return_mat_d(self):
        """
        Diese Methode gibt die Matrix A^(d) as sparse-Matrix zurueck.

        Input: -

        Return:
            (scipy.sparse.dok_matrix-Objekt):
                Die Matrix A^(d) als sparse-Matrix.
        """
        return self.matr

    def anz_nn_abs(self):
        """
        Gibt die Anzahl von Eintraegen von A^(d) zurueck, die ungleich 0 sind.

        Input: -

        Return:
            (int):
                Anzahl von Nicht-Nulleintraegen von A^(d).
        """

        # Array mit Indizes aller Nichtnull-Eintraege von A^(d):

        nn_arr = self.matr.nonzero()[0]

        return len(nn_arr)

    def anz_n_abs(self):
        """
        Gibt die Anzahl von Eintraegen von A^(d) zurueck, die gleich 0 sind.

        Input: -

        Return:
            (int):
                Anzahl von Nulleintraegen von A^(d).
        """

        # Array mit Indizes aller Nichtnull-Eintraege von A^(d):

        nn_arr = self.matr.nonzero()[0]

        # Dimension (Groesse) von A:

        matr_dim = self.matr.get_shape()[0]**2

        return matr_dim - len(nn_arr)

    def anz_nn_rel(self):
        """
        Gibt die relative Anzahl von Eintraegen von A^(d) zurueck, die gleich 0 sind.

        Input: -

        Return:
            (int):
                Relative Anzahl von Nulleintraegen von A^(d).
        """

        # Array mit Indizes aller Nichtnull-Eintraege von A^(d):

        nn_arr = self.matr.nonzero()[0]

        # Dimension (Groesse) von A:

        matr_dim = self.matr.get_shape()[0]**2

        return len(nn_arr)/matr_dim

    def anz_n_rel(self):
        """
        Gibt die relative Anzahl von Eintraegen von A^(d) zurueck, die gleich 0 sind.

        Input: -

        Return:
            (int):
                Relative Anzahl von Nulleintraegen von A^(d).
        """

        # Array mit Indizes aller Nichtnull-Eintraege von A^(d):

        nn_arr = self.matr.nonzero()[0]

        # Dimension (Groesse) von A:

        matr_dim = self.matr.get_shape()[0]**2

        return 1 - len(nn_arr)/matr_dim


if __name__ == "__main__":
    TEST = Sparse(2, 5)
    A = TEST.return_mat_d()
    print(A.todense(), A.get_shape())
    print(TEST.anz_n_rel(), TEST.anz_n_abs(), TEST.anz_nn_abs())
