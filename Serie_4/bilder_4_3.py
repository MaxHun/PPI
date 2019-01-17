import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from aufg_4_1 import KlQuad
from aufg_4_2 import lese
from numpy import random


from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
matplotlib.rcParams.update({'font.size': 30})
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


    mat_lis = [mat_einf, mat_einf[::2,:], mat_einf_10, mat_einf_rand]
    vec_lis = [vec, vec[::2], vec, vec]
    label_lis = ["ungest\"orte Daten", "Datenpunkte mit geradem Index", r"um $+10$ verschoben", "zuf\"allig gest\"ort (normalverteilt)"]

    # Erstellen der Plots in einer for-Schleife: 
    

    plt.figure(figsize=(20, 10))
    ax=plt.subplot(111)
    mat_lis=list(mat_lis[i] for i in [0,3])
    vec_lis=list(vec_lis[i] for i in [0,3])
    label_lis=list(label_lis[i] for i in [0,3])
    #print(mat_lis)
    for ind, mat in enumerate(mat_lis):
        kq_obj = KlQuad(mat, vec_lis[ind])
        lsg_vec = kq_obj.lgs_lsg()


        x = np.linspace(np.min(mat_einf[:, 1]), np.max(mat_einf[:, 1]), 50)
        # 0:.2f
        plt.plot(x, lsg_vec[0] + lsg_vec[1]*x, label=label_lis[ind]+r", $\|r\|={:.2f}$, $\kappa={:.2f}$".format(kq_obj.res()[1], kq_obj.kond()[0]),lw=4)
        plt.xlabel(r"$a_1$")
        plt.ylabel(r"$p$")
        plt.scatter(mat[:, 1], vec_lis[ind],s=100)
    
    # Kosmetik:
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')    
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
    plt.subplots_adjust(left=0.06, bottom=0.09, right=0.99, top=0.99)
    
    minor_locator_x = AutoMinorLocator(2)
    minor_locator_y = AutoMinorLocator(2)
    ax.xaxis.set_minor_locator(minor_locator_x)
    ax.yaxis.set_minor_locator(minor_locator_y)
    
    
    major_locator_x = MultipleLocator(50)
    major_locator_y = MultipleLocator(50)
    ax.xaxis.set_major_locator(major_locator_x)
    ax.yaxis.set_major_locator(major_locator_y)

    plt.legend()
    plt.savefig("Bild.png", dpi=300)
    plt.show()



if __name__ == "__main__":
    main()
