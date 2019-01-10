import csv
import numpy as np

def lese(name, numb={1, 2}):
    """
    Diese Funktion dient zum Einlesen von Werten aus einer Textdatei
    Input:
        mane (String):
            Pfad zur Datei, die eingelesen werden soll
        numb (int):
            Anzahl der zu berücksichtigenden Messungen
    Return:
        ruck(np Array):
            Array mit den zu berücksichtigenden Messungen
    """

    #Einlesen der Datei
    werte = []
    with open(name, newline='') as daten1:
        for zeile in csv.reader(daten1):
            werte.append(zeile)

    #Erstellen daes Rückgabevektors
    laen = len(werte)
    if 0 in numb:
        ruck = np.zeros((laen, len(numb)))
        for i in range(laen):
            kappa = 0
            for j in numb:
                ruck[i][j]=int(werte[i][j])
                kappa = kappa+1
    else:
        ruck = np.zeros((laen, len(numb)+1))
        for i in range(laen):
            kappa = 0
            for j in numb:
                ruck[i][kappa+1]=int(werte[i][j])
                kappa = kappa+1
            ruck[i][0] = 1
    return ruck

print(lese('/u/hnatiuka/Praktikum/PPI/Serie_4/daten1.txt', {1}))
vektb = lese('/u/hnatiuka/Praktikum/PPI/Serie_4/daten1.txt', {0})
mat = lese('/u/hnatiuka/Praktikum/PPI/Serie_4/daten1.txt', {1})

plt.plot(
