"""
sparse.py stellt die Klasse Sparse zur Verfuegung, mit der die Matrix A^(d) für d=1,2,3
bestimmt und analysiert werden kann.
"""

import scipy.sparse as sp
import numpy as np


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
            Mass für die Diskretisierung des zu untersuchenden Gebietes.
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
        self.matr = self.constr_A_d(dim, dis)

    def constr_A_d(self, d, n):
        """
        Konstruiert die Matrix A^(d) mit der gewuenschten Diskretisierung.
        
        Input:
        
            d (int, moegliche Werte: 1, 2, 3):
                Gibt die Raumdimension des untersuchhten Gebietes fest sowie den
                Wert auf der Hauptdiagonale der Koeffizientenmatrix (=2*d).
        
        Return:
            (scipy.sparse.dok_matrix-Objekt):
                A^(d) mit der gewuenschten Diskretisierung.
        """
        if d == 1:

            # im Falle d==1 wird die Koeffizientenmatrix zurueckgegeben:
            
            A = sp.dok_matrix((n-1, n-1))
            A.setdiag(2*d)
            A.setdiag(-1, 1)
            A.setdiag(-1, -1)
            return A

        elif d == 2 or d == 3:
            
            # Anlegen der Matrix:
            
            A = sp.dok_matrix(((n-1)**d,(n-1)**d))
            
            # per for-Schleife wird auf die (n-1)^(d-1)-dimensionale Diagonale
            # die Matrix A^(d-1) gelegt

            for min_ind in (n-1)**(d-1)*np.arange(n-1):
                max_ind = min_ind + (n-1)**(d-1)
                A[min_ind:max_ind, min_ind:max_ind] = self.constr_A_d(d-1 ,n)
            for min_spalt in (n-1)**(d-1)*np.arange(n-2):
                min_zeil = min_spalt + (n-1)**(d-1)
                max_zeil = min_zeil + (n-1)**(d-1)
                max_spalt = min_spalt + (n-1)**(d-1)
                A.setdiag(-1, (n-1)**(d-1))
                A.setdiag(-1, -(n-1)**(d-1))
                return A
        else:
            print("Der Methode constr_A_d wurde ein falscher Wert fuer die Raumdimension d " +
                  "uebergeben. Moeglich sind d=1,2,3")
            return None

    def return_A_d(self):
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

#test = Sparse(2,5)
#A = test.return_A_d()
#print(A.todense(), A.get_shape())
#print(test.anz_n_rel(), test.anz_n_abs(), test.anz_nn_abs())
