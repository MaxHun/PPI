import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from aufg_4_1 import KlQuad
from aufg_4_2 import lese
from numpy import random

matplotlib.rcParams.update({'font.size': 25})

def main():

    # fuer die Matrix zur einfachen Regression muss nur a_1,
    # also die zweite Spalte, ausgelesen werden:

    mat_einf = lese("./daten1.txt", spalt_ind=[1], einsen=True)
    print(mat_einf)
    mat_einf_10 = np.ones_like(mat_einf)
    mat_einf_10[:, 1] = mat_einf[:, 1] + 10
    # mat_einf_rand = np.ones_like(mat_einf)
    # mat_einf_rand[:, 1] = mat_einf[:, 1] + 10*random.randn(12)
    # Die rechte Seite p des zu loesenden Gleichungssystems ergibt sich aus der ersten
    # Spalte:
    print(mat_einf,mat_einf_10)
    vec = lese("./daten1.txt", spalt_ind=[0])

    print(random.randn(12,1).shape, "\n",vec.shape)

    mat_lis = [mat_einf, mat_einf[::4,:], mat_einf_10, mat_einf]
    vec_lis = [vec, vec[::4], vec, vec + 10*random.randn(12, 1)]
    label_lis = ["ungestörte Daten", "Datenpunkte mit geradem Index", "verschoben", "zufällig"]

    # Erstellen der Plots in einer for-Schleife: 
    
    plt.figure(figsize=(20, 10))
    for ind, mat in enumerate(mat_lis):
        kq_obj = KlQuad(mat, vec_lis[ind])
        lsg_vec = kq_obj.lgs_lsg()


        x = np.linspace(np.min(mat_einf[:, 1]), np.max(mat_einf[:, 1]), 50)

        plt.plot(x, lsg_vec[0] + lsg_vec[1]*x, label= label_lis[ind])
        plt.scatter(mat[:, 1], vec_lis[ind])
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

