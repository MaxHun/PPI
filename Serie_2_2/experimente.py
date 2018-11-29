import numpy as np
import sparse
import scipy.sparse as sp
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

def main():
    """
    Hauptprogramm
    """
    fig, ax_arr = plt.subplots(1,1,figsize=(20,10))
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
        ax = ax_arr
        #print(ax)
        ax.loglog(n_arr, anz_n)
        #print(anz_n.min())
    plt.show()

if __name__ == "__main__":
    main()
