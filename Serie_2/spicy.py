class Sparse(object):
    """
    Diese Klasse erlaubt das Plotten von Funktionen und ihren Ableitungen (exakt und
    approximiert).

    Attribute:

        ablex_lis (list):
            Liste aus den ersten drei (anfangend bei 0) exakten Ableitungen der
            zu untersuchenden Funktion. Der list-Index gibt hierbei den Grad der
            Ableitung an, wobei die Funktion selbst als nullte Ableitung aufgefasst wird.
        p_arr (numpy.ndarray aus floats):
            Plotpunkte, an denen die Funktionen geplottet bzw. für die Fehlerbestimmung aus-
            gewertet werden.
    """
    def __init__(slef, ):
        """
        Initialisiert ein neues Differenzieren-Objekt. Legt aus der gegebenen Funktion und deren
        Ableitungen eine Liste an.

        Input:

            fkt (function):
                Bestimmt, wohin die Funktionen gezeichnet werden.
            abl_ex (function):
                Exakte erste Ableitung.
            abl2_ex (function):
                Exakte zweite Ableitung.
            p_arr (numpy.ndarray aus floats):
                Plotpunkte, an denen die Funktionen geplottet bzw. für die Fehlerbestimmung aus-
                gewertet werden.

        Return: -
        """
        self.ablex_lis = [fkt, abl_ex, abl2_ex] # Liste aus exakten Ableitungen
        self.p_arr = p_arr

    def plotfkt_exakt(self, plotbereich, grad=0, **kwargs):
