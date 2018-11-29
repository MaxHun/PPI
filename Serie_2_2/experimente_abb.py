import numpy as np
import sparse
import scipy.sparse as sp
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)


matplotlib.rcParams.update({'font.size': 30})
plt.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',r"\usepackage{nicefrac}"]



def main():
    """
    Hauptprogramm
    """
    fig, ax = plt.subplots(1,1,figsize=(20,10))
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')    
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
    
    #ax_arr = ax_arr.flatten()
    #print(ax_arr[1])
    colors = ["r","g","b"]
    for dim in [1, 2, 3]:
        if dim == 1:
            n_arr = np.unique(np.logspace(np.log10(3), 4, 50, dtype=int))
        if dim == 2:
            n_arr = np.unique(np.logspace(np.log10(3), 2, 50, dtype=int))
        if dim == 3:
            n_arr = np.unique(np.logspace(np.log10(3), 1.3, 20, dtype=int))
        #print(n_arr)
        k=0
        anz_nn = np.zeros(len(n_arr),dtype=float)
        for dis in n_arr:
            sparse_obj_dis = sparse.Sparse(dim,dis)
            print(sparse_obj_dis.anz_n_rel())
            anz_nn[k] = sparse_obj_dis.anz_nn_rel()
            k += 1
        #print(dim-1)    
        #print(ax)
        ax.loglog(n_arr, anz_nn, label=r"Nicht-Null-Eintraege von $A^{{({})}}$ (rel. Anzahl)".format(dim), color=colors[dim-1])
        ax.plot(n_arr, (n_arr-1)**(2*dim), label=r"vollbesetzte Matrix der Groesse $(n-1)^{}$".format(dim), ls="--", color=colors[dim-1])
        ax.axhline(1, ls=":", color="k", alpha=0.6)
        #print(anz_n.min())
        #print(n_arr)
    #for j in np.arange(len(n_arr)):
    #    n_arr[j] = float(n_arr[j])
    n_arr_fl = n_arr.astype(float)
   # for i in [2,-2,-3,-4,-5]:
   #     ax.plot(n_arr_fl, n_arr_fl**i, label="{}".format(i))
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"Eintraege")
    ax.legend(loc=(0.5,0.2), framealpha=1)
    plt.subplots_adjust(left=0.07, right=0.99, bottom=0.09, top=0.99)
    plt.savefig("Bericht/Bilder/nn_eintraege.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()
