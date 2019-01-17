import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from aufg_4_1 import KlQuad
from aufg_4_2 import lese
from numpy import random

matplotlib.rcParams.update({'font.size': 25})

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
matplotlib.rcParams.update({'font.size': 25})
plt.rc('text', usetex=True)
plt.rc('font', family='Open Sans')
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',r"\usepackage{nicefrac}",r"\usepackage[ngerman]{babel}"]


def main():

    # fuer die Matrix zur einfachen Regression muss nur a_1,
    # also die zweite Spalte, ausgelesen werden:

    mat_einf = lese("./daten1.txt", spalt_ind=[1], einsen=True)
    print(mat_einf)
    mat_einf_10 = np.ones_like(mat_einf)
    mat_einf_10[:, 1] = mat_einf[:, 1] + 10
    
    mat_einf_rand = np.ones_like(mat_einf)
    mat_einf_rand[:, 1] = mat_einf[:, 1] + 10*random.randn(12)
    # Die rechte Seite p des zu loesenden Gleichungssystems ergibt sich aus der ersten
    # Spalte:
    print(mat_einf,mat_einf_10)
    vec = lese("./daten1.txt", spalt_ind=[0])


    mat_lis = [mat_einf, mat_einf[::4,:], mat_einf_10, mat_einf_rand]
    vec_lis = [vec, vec[::4], vec, vec]
    label_lis = ["ungest\"orte Daten", "Datenpunkte mit geradem Index", r"um $+10$ verschoben", "zuf\"allig gest\"ort (normalverteilt)"]

    # Erstellen der Plots in einer for-Schleife: 
    

    plt.figure(figsize=(20, 10))
    for ind, mat in enumerate(mat_lis):
        kq_obj = KlQuad(mat, vec_lis[ind])
        lsg_vec = kq_obj.lgs_lsg()


        x = np.linspace(np.min(mat_einf[:, 1]), np.max(mat_einf[:, 1]), 50)
        # 0:.2f
        plt.plot(x, lsg_vec[0] + lsg_vec[1]*x, label=label_lis[ind]+r", $\|r\|={:.2f}$, $\kappa={:.2f}$".format(kq_obj.res()[1], kq_obj.kond()[0]))
        plt.scatter(mat[:, 1], vec_lis[ind])
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()
