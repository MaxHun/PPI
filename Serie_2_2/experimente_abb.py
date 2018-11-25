import numpy as np
import sparse
import scipy.sparse as sp
from matplotlib import pyplot as plt
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)


matplotlib.rcParams.update({'font.size': 25})
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
    for dim in [1, 2, 3]:
        if dim == 1:
            n_arr = np.unique(np.logspace(np.log10(3), 4, 50, dtype=int))
        if dim == 2:
            n_arr = np.unique(np.logspace(np.log10(3), 2, 50, dtype=int))
        if dim == 3:
            n_arr = np.unique(np.logspace(np.log10(3), 1.3, 20, dtype=int))
        #print(n_arr)
        k=0
        anz_n = np.zeros(len(n_arr))
        for dis in n_arr:
            sparse_obj_dis = sparse.Sparse(dim,dis)
            #print(sparse_obj_dis.anz_n_rel())
            anz_n[k] = sparse_obj_dis.anz_n_rel()
            k += 1
        #print(dim-1)    
        #print(ax)
        ax.loglog(n_arr, anz_n, label=r"$d={}$".format(dim))
        #print(anz_n.min())
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
