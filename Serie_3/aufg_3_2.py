"""
Dieses Modul löst die Aufgaben 3.2 und 3.3, indem es die Differentialgleichung löst und
das Verhalten der Lösungen grafisch aufstellt.
"""
from sparse_erw import Sparse
from plot_disc_fct import plot_disc_fct
import matplotlib.pyplot as plt
import numpy as np

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
    if m_nb%(numb-1)==0:
        return(numb-1)
    else:
        return(m_nb%(numb-1))

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
    if dims==1:
        arra = np.zeros(numb-1)
        for i in range(numb-1):
            arra[i] = (i+1)/n
        return(arra)    
    #Dimension 2
    if dims==2:
        arra = np.zeros(((numb-1)**2, 2))
        for i in range((numb-1)**2):
            arra[i] = [modo(i+1, numb)/numb, (i//(numb-1)+1)/numb]
        return(arra)
    #Dimension 3
    if dims == 3:
        arra = np.zeros(((numb-1)**3, 3))
        for i in range((numb-1)**3):
            arra[i] = [modo(i+1, numb)/numb, modo((i//(numb-1)+1), numb)/numb, (i//((numb-1)**2)+1)/numb]
        return(arra)
    
def fkt(x):
    """
    Beispielfunktion
    Input:
        x (float):
            Wert, auf dem die Funktion ausgewertet wird.
    Return:
        (float):
            Wert der Funktion
    """
    return(1000*np.sin(1000*x[0])*(x[1]))

def loesg(numb, dims, fkt, ulsg=fkt):
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
    if dims == 2:
        plot_disc_fct(lsg, numb, "Berechnete Lösung mit Feinheit der Diskretisierung "+str(numb))
        
        
        plot_disc_fct(arrf, numb, "Fehler bezüglich der Referenzlösung mit Feinheit der Diskretisierung "+str(numb))
        plt.show()    
    return(np.amax(arrf))
        
def main():
    """
    In dieser Funktion wird der 
    """
    maxfl = loesg(15, 2, fkt)
    print("Der maximale Fehler ist "+str(maxfl))
    
main()
