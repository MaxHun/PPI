"""
Dieses Programm dient zum Einlesen von Messwerte aus einer .txt Datei und zur grafischen Darstellung
von diesen Werten zusammen mit der linearen Approximation
Arsen Hnatiuk, Max Huneshagen
"""
import csv
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

def lese(name, numb={1, 2}, fall=1):
    """
    Diese Funktion dient zum Einlesen von Werten aus einer Textdatei
    Input:
        mane (String):
            Pfad zur Datei, die eingelesen werden soll
        numb (int):
            Anzahl der zu berücksichtigenden Messungen
        fall (int):
            Kennzeichnet, ob es eine Spalte mit Einsen in die Matrix einzulegen
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
    if fall == 0:
        ruck = np.zeros((laen, len(numb)))
        for i in range(laen):
            kappa = 0
            for j in numb:
                ruck[i][kappa] = int(werte[i][j])
                kappa = kappa+1
    else:
        ruck = np.zeros((laen, len(numb)+1))
        for i in range(laen):
            kappa = 0
            for j in numb:
                ruck[i][kappa+1] = int(werte[i][j])
                kappa = kappa+1
            ruck[i][0] = 1
    return ruck

if __name__ == '__main__':
    #Grafische Darstellung
    print(lese('/u/hnatiuka/Praktikum/PPI/Serie_4/daten1.txt', {1}))
    vektb = lese('/u/hnatiuka/Praktikum/PPI/Serie_4/daten1.txt', {0}, 0)
    mat = lese('/u/hnatiuka/Praktikum/PPI/Serie_4/daten1.txt', {1})
    mat0 = lese('/u/hnatiuka/Praktikum/PPI/Serie_4/daten1.txt', {1}, 0)

    vektb = vektb.flatten()
    mat0 = mat0.flatten()
    plt.figure()
    plt.scatter(mat0, vektb)
    plt.xlabel('Hochwasserstand am Pegel a1')
    plt.ylabel('Hochwasserstand am Pegel p')
    plt.title('Hochwasserstand an verschiedenen Pegeln')
    plt.show()
