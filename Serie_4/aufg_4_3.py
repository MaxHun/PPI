"""
Dieses Skript ist eine Implementierung zur Loesung von Aufgabe 4.3 des PPI.
A. Hnatiuk, M. Huneshagen
"""
from aufg_4_1 import KlQuad
from aufg_4_2 import lese
import numpy as np
from numpy import random
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

matplotlib.rcParams.update({'font.size': 25})




def main_einfach():
    """
    Hauptprogramm zur Berechnung und Darstellung der einfachen linearen Regression. Daten werden
    eingelesen und mit Hilfe der Methode der kleinsten Quadrate linear gefittet. Zudem werden die
    input-Daten gestoert alle Ergebnisse geplottet.

    Input: -

    Return: -
    """
    # fuer die Matrix zur einfachen Regression muss nur a_1,
    # also die zweite Spalte, ausgelesen werden:

    mat_einf = lese("./daten1.txt", spalt_ind=[1], einsen=True)

    # Als Störung werden Verschiebung von a_1 um 10 und eine normalverteilte zufaellige Stoerung
    # gewaehlt (Normalverteilung mit Varianz 1, multipliziert mit 10):

    mat_einf_10 = np.ones_like(mat_einf)
    mat_einf_10[:, 1] = mat_einf[:, 1] + 10
    mat_einf_rand = np.ones_like(mat_einf)
    mat_einf_rand[:, 1] = mat_einf[:, 1] + 10*random.randn(12)

    # Die rechte Seite p des zu loesenden Gleichungssystems ergibt sich aus der ersten
    # Spalte:

    vec = lese("./daten1.txt", spalt_ind=[0])

    # Liste aller zu untersuchenden Matrizen, Vektoren und Beschriftungen:

    mat_lis = [mat_einf, mat_einf[::2, :], mat_einf_10, mat_einf_rand]
    vec_lis = [vec, vec[::2], vec, vec]
    label_lis = ["ungestörte Daten", "Datenpaare mit geradem Index", "verschoben", "zufällig"]

    # Erstellen der Plots in einer for-Schleife:

    plt.figure(figsize=(20, 10))

    for ind, mat in enumerate(mat_lis):

        kq_obj = KlQuad(mat, vec_lis[ind])
        lsg_vec = kq_obj.lgs_lsg()
        x_arr = np.linspace(np.min(mat_einf[:, 1]), np.max(mat_einf[:, 1]), 50)
        plt.plot(x_arr, lsg_vec[0] + lsg_vec[1]*x_arr,
                 label=label_lis[ind]+
                 r", $\|r\|_\infty={:.2f}$, $\kappa={:.1f}$".format(kq_obj.res()[1],
                                                                    kq_obj.kond()[0]))
        plt.scatter(mat[:, 1], vec_lis[ind])

    # Beschriftungen etc.:

    plt.ylabel(r"$p$")
    plt.xlabel(r"$a_1$")
    plt.title(r"Ergebnisse der linearen einfachen Regression")
    plt.legend(prop={'size': 20})
    plt.show()

def main_mehrfach():
    """
    Hauptprogramm zur Berechnung der Mehrfachregression (linear). Daten werden eingelesen, die
    Mehrfachregression wird mit Hilfe der Methode der kleinsten Quadrate ausgefuehrt, die Norm des
    Residuums und die Kondition der Koeffizientenmatrix werden ausgegeben.

    Input: -

    Return: -
    """
    mat_mehrf = lese("./daten1.txt", spalt_ind=[1, 2], einsen=True)
    vec = lese("./daten1.txt", spalt_ind=[0])
    mat_mehrf_10 = np.ones_like(mat_mehrf)
    mat_mehrf_10[:, 1] = mat_mehrf[:, 1] + 10
    mat_mehrf_10[:, 2] = mat_mehrf[:, 2] + 10
    mat_mehrf_rand = np.ones_like(mat_mehrf)
    mat_mehrf_rand[:, 1] = mat_mehrf[:, 1] + 10*random.randn(12)
    mat_mehrf_rand[:, 2] = mat_mehrf[:, 2] + 10*random.randn(12)

    mat_lis = [mat_mehrf, mat_mehrf[::2, :], mat_mehrf_10, mat_mehrf_rand]
    vec_lis = [vec, vec[::2], vec, vec]
    label_lis = ["ungestörte Daten", "Datenpunkte mit geradem Index", "verschoben", "zufällig"]

    for ind, mat in enumerate(mat_lis):
        print("="*50)
        print(label_lis[ind] + ":\n\n")
        kq_obj = KlQuad(mat, vec_lis[ind])
        print("Kondition: {}\n ".format(kq_obj.kond()[0]))
        print("Norm des Residuums: {}\n\n".format(kq_obj.res()[1]))
        print("="*50)

if __name__ == "__main__":
    main_mehrfach()
    main_einfach()
