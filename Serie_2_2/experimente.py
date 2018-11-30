"""
Dieses Skript dient der Untersuchung der Anzahl der Nicht-Null-Eintraege
der Matrix A^(d) fuer d=1,2,3. Dies ist insbesondere deswegen eine wichtige Groesse,
da diese Matrizen hier als scipy.sparse.dok_matrix-Objekte vorliegen, was nur fuer
sehr duenn besetzte Matrizen nennenswerte Vorteile bringt.
Es wird die relative Anzahl der Nicht-Nulleintraege von A^(d) geplottet, zur Orientierung
wird ausserdem eine Linie bei y=1 dargestellt. Darueber hinaus wird die Anzahl von Eintraegen
einer Matrix der gleichen Groesse wie A^(d) im gleichen doppelt-logarithmischen Diagramm geplottet
"""
import numpy as np
import sparse
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


def main():
    """
    Hauptprogramm, das die in __dok__ ausgefuehrte Funktionalitaet besitzt.
    """
    plotb = plt.subplots(1, 1, figsize=(20, 10))[1]

    colors = ["r", "g", "b"]

    for dim in [1, 2, 3]:

        # Aus Laufzeit-Gruenden werden fuer jedes dim andere n-Werte untersucht:

        if dim == 1:
            n_arr = np.unique(np.logspace(np.log10(3), 4, 50, dtype=int))
        if dim == 2:
            n_arr = np.unique(np.logspace(np.log10(3), 2, 50, dtype=int))
        if dim == 3:
            n_arr = np.unique(np.logspace(np.log10(3), 1.3, 20, dtype=int))

        # Ermitteln der Nicht-Null-Eintraege fuer jedes gewuenschte n:

        k = 0
        anz_nn = np.zeros(len(n_arr), dtype=float)
        for dis in n_arr:
            sparse_obj_dis = sparse.Sparse(dim, dis)
            anz_nn[k] = sparse_obj_dis.anz_nn_rel()
            k += 1

        # Plotbefehle:

        plotb.loglog(n_arr, anz_nn, label=r"Nicht-Null-Eintraege von " +
                     r"$A^{{({})}}$ (rel. Anzahl)".format(dim), color=colors[dim-1])
        plotb.plot(n_arr, (n_arr-1)**(2*dim), label=r"vollbesetzte Matrix der Groesse " +
                   r"$(n-1)^{}$".format(dim), ls="--", color=colors[dim-1])
        plotb.axhline(1, ls=":", color="k", alpha=0.6)

    plotb.set_xlabel(r"$n$")
    plotb.set_ylabel(r"Eintraege")
    plotb.legend(loc="best", framealpha=1)
    plt.show()

if __name__ == "__main__":
    print(__doc__)
    main()
