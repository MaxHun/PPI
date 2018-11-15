class Sparse(object):
    """
    Diese Klasse erlaubt das Erstellen der Matrizen A^(d) für d in [1,2,3]. Diese Matrizen werden
    z. B. für die Berechnung der DGL u''(x)=-f(x) verwendet. Es handelt sich bei diesen Matrizen
    um sehr dünn besetzte Block-Band-Matrizen, was die Verwendung von sog. sparse-Matrizen
    in der numerischen Umsetzung nahelegt.

    Attribute:

        :
            Liste aus den ersten drei (anfangend bei 0) exakten Ableitungen der
            zu untersuchenden Funktion. Der list-Index gibt hierbei den Grad der
            Ableitung an, wobei die Funktion selbst als nullte Ableitung aufgefasst wird.
        p_arr (numpy.ndarray aus floats):
            Plotpunkte, an denen die Funktionen geplottet bzw. für die Fehlerbestimmung aus-
            gewertet werden.
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

    def a_d(self):
        """
        Diese Methode gibt die Matrix A^(d) als sparse-Matrix zurück.

        Input: -

        Return:
            (scipy.sparse.dok_matrix-Objekt):
                Die Matrix A^(d) als sparse-Matrix.
        """
        return True

    def anz_nn(self):
        """
        Gibt die Anzahl von Einträgen von A^(d) zurück, die ungleich 0 sind.

        Input: -

        Return:
            (int):
                Anzahl von Nicht-Nulleinträgen von A^(d).
        """
        return True
