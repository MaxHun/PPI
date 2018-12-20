"""
Dieses Modul löst die Aufgaben 3.2 und 3.3, indem es die Differentialgleichung löst und
das Verhalten der Lösungen grafisch aufstellt.
"""
from plot_disc_fct import plot_disc_fct
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from sparse_erw import Sparse

def modo(m_nb, numb):
    """
    Funktion, die die modofizierte Modolo Methode aus dem Bericht zu Serie 2 implementiert
    Input:
        m_nb (int):
            Zahl, für die wir den Wert der modifizierten Modolo Methode berechnen wollen
        numb (int):
            Feinheit der Diskretisierung
    Return:
        (int):
            Ausgabe der modifizierten Modolo Methode
    """
    if m_nb%(numb-1) == 0:
        return numb-1
    return m_nb%(numb-1)

def gitter(numb, dims):
    """
    Funktion, die für eine gegebene Dimension und Schritweite eine Menge von Punkten erzeugt, auf
    der die Differentialgleichung zu lösen ist.
    Input:
        numb (int):
            Feinheit der Diskretisierung
        dims (int):
            Dimension der Diskretisierung
    Return:
        arra (ndarray):
            Array mit den Punkten auf dem Diskretisierungsgitter
    """
    #Dimension 1
    if dims == 1:
        arra = np.zeros(numb-1)
        for i in range(numb-1):
            arra[i] = (i+1)/numb
        return arra
    #Dimension 2
    if dims == 2:
        arra = np.zeros(((numb-1)**2, 2))
        for i in range((numb-1)**2):
            arra[i] = [modo(i+1, numb)/numb, (i//(numb-1)+1)/numb]
        return arra
    #Dimension 3
    arra = np.zeros(((numb-1)**3, 3))
    for i in range((numb-1)**3):
        arra[i] = [modo(i+1, numb)/numb, modo((i//(numb-1)+1), numb)/numb,
                   (i//((numb-1)**2)+1)/numb]
    return arra

def fntn1(wert):
    """
    Beispielfunktion der Dimension 1
    Input:
        wert (float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return 2

def fntn2(wert):
    """
    Beispielfunktion der Dimension 2
    Input:
        wert (array von float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return 2*(wert[0]*(1-wert[0])+wert[1]*(1-wert[1]))

def fntn3(wert):
    """
    Beispielfunktion der Dimension 3
    Input:
        wert (array von float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return 2*(wert[0]*(1-wert[0])*wert[2]*(1-wert[2])+wert[1]*(1-wert[1])*wert[0]*(1-wert[0])+
             wert[1]*(1-wert[1])*wert[2]*(1-wert[2]))

def ulsg1(wert):
    """
    Exakte Lösung der Dimension 1
    Input:
        wert (float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return wert*(1-wert)

def ulsg2(wert):
    """
    Exakte Lösung der Dimension 2
    Input:
        wert (array von float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return wert[0]*(1-wert[0])*wert[1]*(1-wert[1])

def ulsg3(wert):
    """
    Exakte Lösung der Dimension 3
    Input:
        wert (array von float):
            Werte, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return wert[0]*(1-wert[0])*wert[1]*(1-wert[1])*wert[2]*(1-wert[2])

def loesg(numb, dims, fkt, ulsg):
    """
    Diese Methode dient zur Lösung der Differentialgleichung und zum Vergleichen der exakten
    und approxmierten Lösungen.
    Input:
        numb (int):
            Feinheit der Diskretisierung
        dims (int):
            Dimension der Diskretisierung
        fkt (Funktion):
            Die gegebene Funktion f aus der Aufgabestellung
        ulsg (Funktion):
            Die exakte Lösung der Differentialgleichung

    Return:
        (float):
            Der absolute Fehler in der approximierten Lösung der Differentialgleichung
    """
    #Erstellung des Vektors b
    arra = gitter(numb, dims)
    arrb = np.zeros((numb-1)**dims)
    for i in range((numb-1)**dims):
        arrb[i] = fkt(arra[i])

    #Erstellung und Lösen der Bandmatrix
    mata = Sparse(dims, numb)
    lsg = mata.lgs_lsg(arrb)

    #Erstellung des Vektors der exakten Lösung
    arrex = np.zeros((numb-1)**dims)
    for i in range((numb-1)**dims):
        arrex[i] = ulsg(arra[i])

    #Erstellung des Vektors des Fehlers in der berechneten Lösung
    arrf = np.zeros((numb-1)**dims)
    for i in range((numb-1)**dims):
        arrf[i] = np.abs(arrex[i]-lsg[i])

    #Grafische Ausgabe
    for i in [7, 11]
        
        #Erstellung des Vektors b
        arra = gitter(numb, dims)
        arrb = np.zeros((numb-1)**dims)
        for i in range((numb-1)**dims):
            arrb[i] = fkt(arra[i])

        #Erstellung und Lösen der Bandmatrix
        mata = Sparse(dims, numb)
        lsg = mata.lgs_lsg(arrb)

        #Erstellung des Vektors der exakten Lösung
        arrex = np.zeros((numb-1)**dims)
        for i in range((numb-1)**dims):
            arrex[i] = ulsg(arra[i])

        #Erstellung des Vektors des Fehlers in der berechneten Lösung
        arrf = np.zeros((numb-1)**dims)
        for i in range((numb-1)**dims):
            arrf[i] = np.abs(arrex[i]-lsg[i])

        #Plot der berechneten Lösung
        plot_disc_fct(lsg, numb, "Berechnete Lösung mit Feinheit der Diskretisierung "+str(numb))

        #Plot der Referenzlösung
        grd1 = np.linspace(0, 1, 1000)
        grd2 = np.linspace(0, 1, 1000)
        grd1, grd2 = np.meshgrid(grd1, grd2)
        arra2 = gitter(1001, 2)
        arrex2 = np.zeros(1000000)
        for i in range(1000000):
            arrex2[i] = ulsg(arra2[i])
        grd3 = arrex2.reshape(1000, 1000)
        fig = plt.figure()
        fig.suptitle("Die Referenzlösung")
        axis = Axes3D(fig)
        axis.plot_surface(grd1, grd2, grd3, cmap=cm.coolwarm)
        axis.view_init(20, -105)

        #Plot des Fehlers
        plot_disc_fct(arrf, numb, "Fehler bezüglich der Referenzlösung mit"
                    +" Feinheit der Diskretisierung "+str(numb))
    plt.show()
        
    

    return np.amax(arrf)

def main():
    """
    In dieser Funktion werden alle Lösungen der Aufgabe dem Nutzer ausgegeben
    """
    dims = 2
    numb = 5
    fntn = [fntn1, fntn2, fntn3]
    ulsg = [ulsg1, ulsg2, ulsg3]
    maxfl = loesg(numb, dims, fntn[dims-1], ulsg[dims-1])
    print("Der maximale Fehler ist "+str(maxfl))

main()
