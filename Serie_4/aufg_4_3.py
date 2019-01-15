import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from aufg_4_1 import KlQuad
from aufg_4_2 import lese

matplotlib.rcParams.update({'font.size': 25})

def main():

    # fuer die Matrix zur einfachen Regression muss nur a_1,
    # also die zweite Spalte, ausgelesen werden:
    mat_einf = lese("./daten1.txt", spalt_ind=[1], einsen=True)
    
    # Die rechte Seite p des zu loesenden Gleichungssystems ergibt sich aus der ersten
    # Spalte:

    vec = lese("./daten1.txt", spalt_ind=[0])
    
    # Anlegen des KlQuad-Objektes und Loesen des Gleichungssystems:

    kq_obj = KlQuad(mat_einf, vec)
    lsg_vec = kq_obj.lgs_lsg()
    
    x = np.linspace(np.min(mat_einf[:, 1]), np.max(mat_einf[:, 1]), 50)
    plt.figure(figsize=(20, 10))
    plt.plot(x, lsg_vec[0] + lsg_vec[1]*x)
    plt.scatter(mat_einf[:, 1], vec)
    plt.show()
    
    a_1 = mat_einf[:1]
    print(a_1)

if __name__ == "__main__":
    main()

