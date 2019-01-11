"""
Diese Datei enthaelt im Wesentlichen die Funktion lese, mit der eine Textdatei mit Messwerten
ausgelesen werden kann.
"""
import numpy as np



def lese(name, zeil_ind=None, spalt_ind=None, einsen=False):
    """
    Dient dem Einlesen einer Textdatei mit Messwerten.

    Input:

        name (str):
            Pfad zur zu untersuchenden Textdatei.
        zeil_ind (lis oder array, optional, sonst: None):
            Indizes der Zeilen, die beruecksichtigt werden sollen.
        spalt_ind (lis oder array, optional, sonst: None):
            Indizes der Spalten, die beruecksichtigt werden sollen.
        einsen (bool):
            Gibt an, ob die erste Spalte der ausgegebenen Matrix mit Einsen gefuellt werden soll,
            was fuer die lineare Regression mit Verschiebung nuetzlich ist.
    """
    dat = np.loadtxt(name, delimiter=",")

    if zeil_ind is None:
        zeil_ind = np.arange(dat.shape[0])
    if spalt_ind is None:
        spalt_ind = np.arange(dat.shape[1])

    # Nur die gewuenschten Zeilen und Spalten auswählen:

    dat = dat[zeil_ind[:, None], spalt_ind]

    # Einsen in die erste Spalte, falls gewuenscht:

    if einsen is True:
        eins_arr = np.ones((dat.shape[0], 1))
        dat = np.hstack((eins_arr, dat))

    return dat


if __name__ == "__main__":
    lese("./daten1.txt", np.array([0, 2, 3, 4]), np.array([0, 2]), True)
